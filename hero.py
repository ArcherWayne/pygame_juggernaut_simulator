import pygame
from setting import *
from debug import debug

class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, name, health, movement_speed, damage, foreswing, backswing):
        super(Hero, self).__init__(groups)

        # attributes
        self.name = name
        self.health = health
        self.max_health = self.health
        self.health_percentage = self.health/self.max_health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = foreswing
        self.backswing = backswing

        # image and rect
        self.hero_surface = pygame.transform.scale(
            pygame.image.load('assets/hero/juggernaut.png').convert_alpha(), (HERO_HEIGHT, HERO_WIDTH)
        )
        # 以下两行只能名字叫做image和rect, 这是pygame定义的draw函数中规定的
        self.image = self.hero_surface
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        
        # movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy() # old_rect是用来检测碰撞的一部分, 不是dt中的一部分

        # varibles init
        self.flag_moving = 0
        self.target_pos = (0,0)

    def get_dt(self, dt):
        self.dt = dt
    
    def keyboard_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.flag_moving = 0
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.flag_moving = 0
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.flag_moving = 0
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.flag_moving = 0
            self.direction.x = 1
        else:
            self.direction.x = 0

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.movement_speed * self.dt
        self.rect.x = round(self.pos.x)
        self.pos.y += self.direction.y * self.movement_speed * self.dt
        self.rect.y = round(self.pos.y)

    def init_mouse_movement(self, mouse_click_pos):
        self.target_pos = mouse_click_pos
        if self.rect.midbottom != mouse_click_pos:
            self.flag_moving = 1

    def mouse_movement(self):
        if self.flag_moving:
            self.direction.y = self.target_pos[1] - self.rect.midbottom[1]
            self.direction.x = self.target_pos[0] - self.rect.midbottom[0]

            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.pos.x += self.direction.x * self.movement_speed * self.dt
            self.rect.x = round(self.pos.x)
            self.pos.y += self.direction.y * self.movement_speed * self.dt
            self.rect.y = round(self.pos.y)

        if self.rect.midbottom == self.target_pos:
            self.flag_moving = 0

    def boundary(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.x

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
            self.pos.x = self.rect.x

        if self.rect.top < 0:
            self.rect.top = 0
            self.pos.y = self.rect.y

        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.pos.y = self.rect.y
    
    
    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 42, self.rect.midtop[1] - 22, 84, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 40, self.rect.midtop[1] - 20, round(80 * self.health_percentage), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)
    
    
    def update(self):
        self.old_rect = self.rect.copy()
        self.keyboard_movement()
        self.mouse_movement()
        self.boundary()
        self.draw_health_bar()