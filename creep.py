import pygame
import math
from setting import *
from debug import debug


class Creep(pygame.sprite.Sprite):
    def __init__(self, groups, health, movement_speed, damage, spawn_location, hero):
        super(Creep, self).__init__(groups)

        # attributes
        self.health = health
        self.max_health = self.health
        self.health_percentage = self.health/self.max_health
        self.movement_speed = movement_speed
        self.damage = damage

        # image and rect
        self.creep_enemy_surface = pygame.transform.scale(
            pygame.image.load(
                'assets/creep/player_stand.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
        )
        self.image = self.creep_enemy_surface
        self.rect = self.image.get_rect(center=spawn_location)

        creep_walk_1_right = pygame.transform.scale(
            pygame.image.load(
                'assets/creep/player_walk_1.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
        )
        creep_walk_2_right = pygame.transform.scale(
            pygame.image.load(
                'assets/creep/player_walk_2.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
        )
        creep_walk_1_left = pygame.transform.flip(creep_walk_1_right, 1, 0)
        creep_walk_2_left = pygame.transform.flip(creep_walk_2_right, 1, 0)
        self.creep_walk_left = [creep_walk_1_left, creep_walk_2_left]
        self.creep_walk_right = [creep_walk_1_right, creep_walk_2_right]

        # movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy()  # old_rect是用来检测碰撞的一部分 不是dt中的一部分
        self.facing_direction = 0

        # state check
        self.idle_state = 1
        self.moving_state = 0

        # varibles init
        self.hero = hero
        self.flag_moving = 0
        self.target_pos = (0, 0)
        self.movement_animation_index = 0

    def get_dt(self, dt):
        self.dt = dt

    def movement(self):
        self.distance_with_hero = int(math.sqrt(math.pow((self.rect.midbottom[0] - self.hero.rect.midbottom[0]), 2)
                                                + math.pow((self.rect.midbottom[1] - self.hero.rect.midbottom[1]), 2)))

        if self.distance_with_hero > 60:
            self.flag_moving = 1
        elif self.distance_with_hero <= 60:
            self.flag_moving = 0

        # debug(self.flag_moving, 10, 30, 'self.flag_moving')

        if self.flag_moving:
            self.target_pos = self.hero.rect.midbottom

            self.direction.y = self.target_pos[1] - self.rect.midbottom[1]
            self.direction.x = self.target_pos[0] - self.rect.midbottom[0]

            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.pos.x += self.direction.x * self.movement_speed * self.dt
            self.rect.x = round(self.pos.x)
            self.pos.y += self.direction.y * self.movement_speed * self.dt
            self.rect.y = round(self.pos.y)

    def creep_facing_direction(self):
        if self.old_rect.x < self.rect.x:
            self.facing_direction = 1
        elif self.old_rect.x > self.rect.x:
            self.facing_direction = 0

    def creep_state_check(self):
        # update creep state
        if self.old_rect.x != self.rect.x or self.old_rect.y != self.rect.y:
            self.idle_state = 0
            self.moving_state = 1
        else:
            self.idle_state = 1
            self.moving_state = 0

        self.state_check_list = [self.idle_state, self.moving_state]
        

    def creep_state_animation(self):
        if self.state_check_list[0]: # 检查静止不动状态
            self.image = self.creep_enemy_surface

        if self.state_check_list[1]: # 检查移动状态
            if self.facing_direction == 0: # facing left
                self.movement_animation_index += 0.1
                if self.movement_animation_index >= len(self.creep_walk_left):
                    self.movement_animation_index = 0
                self.image = self.creep_walk_left[int(self.movement_animation_index)]

            if self.facing_direction == 1: # facing right
                self.movement_animation_index += 0.1
                if self.movement_animation_index >= len(self.creep_walk_right):
                    self.movement_animation_index = 0
                self.image = self.creep_walk_right[int(self.movement_animation_index)]

    def draw_health_bar(self):
        health_bar_background = pygame.Rect(
            self.rect.midtop[0] - 32, self.rect.midtop[1] - 22, 64, 12)
        health_bar_content = pygame.Rect(
            self.rect.midtop[0] - 30, self.rect.midtop[1] - 20, round(60 * self.health_percentage), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def update(self):
        self.old_rect = self.rect.copy()
        self.movement()
        self.creep_facing_direction()
        self.creep_state_check()
        self.creep_state_animation()
        self.draw_health_bar()
