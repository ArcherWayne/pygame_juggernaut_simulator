import pygame
import math
from animation_manager import AnimationManager
from setting import *
from debug import debug
from clip import clip

class Creep(pygame.sprite.Sprite):
    def __init__(self, groups, health, movement_speed, damage, spawn_location, hero, collision_groups, animation_mananger):
        super(Creep, self).__init__(groups)

        # attributes
        self.health = health
        self.max_health = self.health
        self.health_percentage = self.health/self.max_health
        self.movement_speed = movement_speed
        self.damage = damage
        self.animation_mananger = animation_mananger

        # collision
        self.collision_groups = collision_groups
        # self.collision_rect = pygame.Rect(0, 0, CREEP_WIDTH/2, CREEP_HEIGHT/2)
        # self.old_collision_rect = self.collision_rect.copy()

        # image and rect
        # idle_animation
        idle_image = pygame.image.load(
            'assets/creep/creep_idle_animation.png').convert_alpha()
        idle_animation_frame_1_right = pygame.transform.scale(
            clip(idle_image, 0, 0, 96, 96), (CREEP_HEIGHT, CREEP_WIDTH))
        idle_animation_frame_2_right = pygame.transform.scale(
            clip(idle_image, 0, 96, 96, 96), (CREEP_HEIGHT, CREEP_WIDTH))

        idle_animation_frame_1_left = pygame.transform.flip(
            idle_animation_frame_1_right, 1, 0)
        idle_animation_frame_2_left = pygame.transform.flip(
            idle_animation_frame_2_right, 1, 0)

        self.idle_animation_list_right = [
            idle_animation_frame_1_right, idle_animation_frame_2_right]
        self.idle_animation_list_left = [
            idle_animation_frame_1_left, idle_animation_frame_2_left]

        # walking_animation
        walking_image = pygame.image.load(
            'assets/creep/creep_walking_animation.png').convert_alpha()
        walking_animation_frame_1_right = pygame.transform.scale(
            clip(walking_image, 0, 0, 96, 96), (CREEP_HEIGHT, CREEP_WIDTH))
        walking_animation_frame_2_right = pygame.transform.scale(
            clip(walking_image, 0, 96, 96, 96), (CREEP_HEIGHT, CREEP_WIDTH))

        walking_animation_frame_1_left = pygame.transform.flip(
            walking_animation_frame_1_right, 1, 0)
        walking_animation_frame_2_left = pygame.transform.flip(
            walking_animation_frame_2_right, 1, 0)

        self.walking_animation_list_right = [walking_animation_frame_1_right, walking_animation_frame_2_right]
        self.walking_animation_list_left = [walking_animation_frame_1_left, walking_animation_frame_2_left]
        
        # init animation
        self.image = idle_animation_frame_1_right
        self.rect = self.image.get_rect(center=spawn_location)

        # attack animation
        attack_image = pygame.image.load(
            'assets/creep/creep_attack_animation.png').convert_alpha()
        self.attack_animation_frame_1_right = pygame.transform.scale(
            clip(attack_image, 0, 0, 96, 96), (CREEP_HEIGHT, CREEP_WIDTH))
        walking_animation_frame_1_left = pygame.transform.flip(
            walking_animation_frame_1_right, 1, 0)

        # movement
        self.pos = pygame.math.Vector2(self.rect.midbottom)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy()  # old_rect是用来检测碰撞的一部分 不是dt中的一部分
        self.facing_direction = 0

        # state check
        self.idle_state = 1
        self.moving_state = 0
        self.attacking_state = 0

        self.state_check_list = [self.idle_state, self.moving_state, self.attacking_state]

        # aggro
        self.aggro_target = []

        # varibles init
        self.hero = hero
        self.flag_moving = 0
        self.target_pos = (0, 0)
        self.idle_animation_index = 0
        self.movement_animation_index = 0

    def get_dt(self, dt):
        self.dt = dt

    def aggro_check(self):
        self.aggro_target = self.hero

        self.distance_with_target = int(math.sqrt(math.pow((self.rect.midbottom[0] - self.aggro_target.rect.midbottom[0]), 2)
                                                + math.pow((self.rect.midbottom[1] - self.aggro_target.rect.midbottom[1]), 2)))

        if 60 < self.distance_with_target < 150:
            self.flag_moving = 1
        else:
            self.flag_moving = 0

    def movement(self):
        if self.flag_moving:
            self.target_pos = self.aggro_target.rect.midbottom

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

        self.state_check_list = [self.idle_state, self.moving_state, self.attacking_state]

    def creep_state_animation(self):
        if self.state_check_list[0]: # 检查静止不动状态
            self.idle_animation_index += 1/20
            if self.facing_direction == 1: # facing right
                if self.idle_animation_index >= len(self.idle_animation_list_right):
                    self.idle_animation_index = 0
                self.image = self.idle_animation_list_right[int(
                    self.idle_animation_index)]

            elif self.facing_direction == 0: # facing left
                if self.idle_animation_index >= len(self.idle_animation_list_left):
                    self.idle_animation_index = 0
                self.image = self.idle_animation_list_left[int(
                    self.idle_animation_index)]

        if self.state_check_list[1]: # 检查移动状态
            if self.facing_direction == 0: # facing left
                self.movement_animation_index += 1/15
                if self.movement_animation_index >= len(self.walking_animation_list_left):
                    self.movement_animation_index = 0
                self.image = self.walking_animation_list_left[int(self.movement_animation_index)]

            if self.facing_direction == 1: # facing right
                self.movement_animation_index += 1/15
                if self.movement_animation_index >= len(self.walking_animation_list_right):
                    self.movement_animation_index = 0
                self.image = self.walking_animation_list_right[int(self.movement_animation_index)]

        if self.state_check_list[2]:
            pass

    def draw_health_bar(self):
        self.health_percentage = self.health/self.max_health
        health_bar_background = pygame.Rect(
            self.rect.midtop[0] - 32, self.rect.midtop[1] - 22, 64, 12)
        health_bar_content = pygame.Rect(
            self.rect.midtop[0] - 30, self.rect.midtop[1] - 20, round(60 * self.health_percentage), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def creep_attacked(self, damage):
        self.health -= damage
        self.animation_mananger.init_animation('blood_animation', self.rect.center)

    def death_check(self):
        if self.health <= 0:
            pygame.sprite.Sprite.kill(self)

    def collision_detection(self):
        self.collision('horizontal')
        self.collision('vertical')

    def collision(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self, self.collision_groups, False)
        if collision_sprites:
            if direction == 'horizontal':
                for sprite in collision_sprites:
                    # collision on the right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x

                    # collision on the left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x

            if direction == 'vertical':
                for sprite in collision_sprites:
                    # collision on the bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y

                    # collision on the top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y

    def update(self):
        self.old_rect = self.rect.copy()

        self.aggro_check()
        self.movement()
        self.collision_detection()
        self.creep_facing_direction()
        self.creep_state_check()
        self.creep_state_animation()
        self.draw_health_bar()
        self.death_check()
