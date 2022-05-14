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
            pygame.image.load('assets/creep/player_stand.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
            )
        self.image = self.creep_enemy_surface
        self.rect = self.image.get_rect(center=spawn_location)

        creep_walk_1 = pygame.transform.scale(
            pygame.image.load('assets/creep/player_walk_1.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
            )
        creep_walk_2 = pygame.transform.scale(
            pygame.image.load('assets/creep/player_walk_2.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
            )
        self.creep_walk = [creep_walk_1, creep_walk_2]

        # movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy() # old_rect是用来检测碰撞的一部分, 不是dt中的一部分 

        # varibles init
        self.hero = hero
        self.flag_moving = 0
        self.target_pos = (0,0)
        self.movement_animation_index = 0

    def get_dt(self, dt):
        self.dt = dt

    def movement(self):
        self.distance_with_hero = int(math.sqrt(math.pow((self.rect.midbottom[0] - self.hero.rect.midbottom[0]) ,2)\
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
            
            # debug(self.target_pos, 10, 10, "self.target_pos")

    def movement_animation(self):
        if self.flag_moving:
            self.movement_animation_index += 0.1
            if self.movement_animation_index >= len(self.creep_walk):
                self.movement_animation_index = 0

            self.image = self.creep_walk[int(self.movement_animation_index)]
        elif ~self.flag_moving:
            self.image = self.creep_enemy_surface

    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 32, self.rect.midtop[1] - 22, 64, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 30, self.rect.midtop[1] - 20, round(60* self.health_percentage), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)


    def update(self):
        self.movement()
        self.movement_animation()
        self.draw_health_bar()

