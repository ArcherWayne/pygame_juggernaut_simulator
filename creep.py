import pygame
from setting import *
from debug import debug


class Creep(pygame.sprite.Sprite):
    def __init__(self, groups, health, movement_speed, damage, spawn_location, hero):
        super(Creep, self).__init__(groups)

        # attributes
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage

        # image and rect
        self.creep_enemy_surface = pygame.transform.scale(
            pygame.image.load('assets/creep/player_stand.png').convert_alpha(), (CREEP_HEIGHT, CREEP_WIDTH)
        )
        self.image = self.creep_enemy_surface
        self.rect = self.image.get_rect(center=spawn_location)

        # movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy() # old_rect是用来检测碰撞的一部分, 不是dt中的一部分 

        # varibles init
        self.hero = hero
        

    def get_dt(self, dt):
        self.dt = dt

    def movement(self):
        debug('self.hero.rect.midbottom', self.hero.rect.midbottom)
        # debug(self.hero.pos, 10, 30)

    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 32, self.rect.midtop[1] - 22, 64, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 30, self.rect.midtop[1] - 20,
                                         60 * (self.health / CREEP_HEALTH), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)


    def update(self):
        self.movement()
        self.draw_health_bar()

