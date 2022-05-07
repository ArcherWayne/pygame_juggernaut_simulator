from random import random

import pygame
from setting import *


class Creep(pygame.sprite.Sprite):
    def __init__(self, groups, health, movement_speed, damage, spawn_location):
        super(Creep, self).__init__(groups)
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.collision_index = 0

        self.creep_enemy_surface = pygame.transform.scale(
            pygame.image.load('assets/creep_enemy.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
        )
        self.image = self.creep_enemy_surface
        self.rect = self.image.get_rect(center=spawn_location)

        self.health_reduce_index = 0

    def movement(self, hero_pos):
        pass
        # distance_hero_creep = math.sqrt(math.pow(hero_pos[0] - self.rect.x, 2) + math.pow(hero_pos[1] - self.rect.y, 2))
        # if distance_hero_creep >= 60:
        #
        #     y_distance = self.rect.midbottom[1] - hero_pos[1]
        #     x_distance = self.rect.midbottom[0] - hero_pos[0]
        #
        #     y_speed = int(math.sqrt(
        #         math.pow(self.movement_speed, 2) / (math.pow((x_distance / y_distance), 2) + 1)
        #     )) if y_distance != 0 else 0
        #     x_speed = int(math.sqrt(
        #         math.pow(self.movement_speed, 2) / (math.pow((y_distance / x_distance), 2) + 1)
        #     )) if x_distance != 0 else 0
        #
        #     if y_distance < 0:
        #         self.rect.y += y_speed
        #     elif y_distance > 0:
        #         self.rect.y -= y_speed
        #     if x_distance < 0:
        #         self.rect.x += x_speed
        #     elif x_distance > 0:
        #         self.rect.x -= x_speed

    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 32, self.rect.midtop[1] - 22, 64, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 30, self.rect.midtop[1] - 20,
                                         60 * (self.health / CREEP_HEALTH), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def destroy(self):
        if self.health <= 0:
            self.kill()

    def attack(self):
        pass

    def health_reduce(self):
        self.health_reduce_index += 1
        if self.health > setting.CREEP_CIT_HEALTH:
            if self.health_reduce_index >= 120:
                self.health -= random.randint(9, 12)
                self.health_reduce_index = 0

        if self.health <= setting.CREEP_CIT_HEALTH:
            self.creep_enemy_surface = pygame.transform.scale(
                pygame.image.load('assets/graphics/Player/jump.png').convert_alpha(), (60, 60)
            )
            self.image = self.creep_enemy_surface
            if self.health_reduce_index >= 160:
                self.kill()
                self.health_reduce_index = 0

    def update(self, hero_pos):
        self.movement(hero_pos)
        self.attack_interval()
        self.health_reduce()
        self.draw_health_bar()
        self.destroy()
