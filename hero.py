import pygame
import math
import creep
import hero_skill
from debug import debug
from clip import clip
from setting import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, name, health, movement_speed, damage, foreswing, backswing):
        super(Hero, self).__init__(groups)
        # attributes -------------------------------------------------------------------------------- #
        self.name = name
        self.health = health
        self.max_health = self.health
        self.health_percentage = self.health/self.max_health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = foreswing
        self.backswing = backswing

        # image and rect ---------------------------------------------------------------------------- #
        
        # self.hero_surface = pygame.transform.scale(
        #     pygame.image.load(
        #         'assets/hero/juggernaut.png').convert_alpha(), (HERO_HEIGHT, HERO_WIDTH)
        # )
        # # 以下两行只能名字叫做image和rect, 这是pygame定义的draw函数中规定的
        # self.image = self.hero_surface
        # self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        idle_image = pygame.image.load('assets/hero/hero_idle_animation.png').convert_alpha()
        idle_animation_frame_1 = pygame.transform.scale(clip(idle_image, 0, 0, 96, 96), (HERO_HEIGHT, HERO_WIDTH))
        idle_animation_frame_2 = pygame.transform.scale(clip(idle_image, 0, 96, 96, 96), (HERO_HEIGHT, HERO_WIDTH))
        idle_animation_frame_3 = pygame.transform.scale(clip(idle_image, 0, 192, 96, 96), (HERO_HEIGHT, HERO_WIDTH))
        self.idle_animation_list = [idle_animation_frame_1, idle_animation_frame_2, idle_animation_frame_3, idle_animation_frame_2]
        self.movement_animation_list = []
        self.image = idle_animation_frame_1
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        # movement ---------------------------------------------------------------------------------- #
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy()  # old_rect是用来检测碰撞的一部分, 不是dt中的一部分

        # state check ------------------------------------------------------------------------------- #
        self.idle_state = 1
        self.moving_state = 0
        self.attacking_state = 0
        self.skill_1_state = 0
        self.skill_2_state = 0
        self.skill_3_state = 0
        self.skill_4_state = 0

        # varibles init ----------------------------------------------------------------------------- #
        self.flag_moving = 0
        self.target_pos = (0, 0)
        self.idle_animation_index = 0

    def get_dt(self, dt):
        self.dt = dt

    def hero_state_check(self):
        # check idle and movement state
        if self.old_rect.x != self.rect.x or self.old_rect.y != self.rect.y:
            self.idle_state = 0
            self.moving_state = 1
        else:
            self.idle_state = 1
            self.moving_state = 0

        self.state_check_list = [self.idle_state, self.moving_state, self.attacking_state,
                                 self.skill_1_state, self.skill_2_state, self.skill_3_state, self.skill_4_state, ]

    def hero_state_animation(self):
        if self.state_check_list[0]:
            self.idle_animation_index += 1/30
            if self.idle_animation_index >= len(self.idle_animation_list):
                self.idle_animation_index = 0
            self.image = self.idle_animation_list[int(self.idle_animation_index)]
        if self.state_check_list[1]:
            pass
        if self.state_check_list[2]:
            pass
        if self.state_check_list[3]:
            pass
        if self.state_check_list[4]:
            pass       
        if self.state_check_list[5]:
            pass
        if self.state_check_list[6]:
            pass


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

        if math.sqrt(math.pow((self.rect.midbottom[0]-self.target_pos[0]), 2) +
                     math.pow((self.rect.midbottom[1]-self.target_pos[1]), 2)) <= 3:
            self.pos.y = self.target_pos[1] - HERO_HEIGHT
            self.pos.x = self.target_pos[0] - HERO_WIDTH/2
            self.rect.y = self.pos.y
            self.rect.x = self.pos.x

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
        health_bar_background = pygame.Rect(
            self.rect.midtop[0] - 42, self.rect.midtop[1] - 22, 84, 12)
        health_bar_content = pygame.Rect(
            self.rect.midtop[0] - 40, self.rect.midtop[1] - 20, round(80 * self.health_percentage), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def hero_use_skill(self, pressed_key):
        match pressed_key:
            case 1:
                hero_skill.blade_fury(self, creep)
            case 2:
                hero_skill.healing_ward()
            case 3:
                hero_skill.blade_dance()
            case 4:
                hero_skill.swiftslash()

    def update(self):
        self.old_rect = self.rect.copy()
        self.keyboard_movement()
        self.mouse_movement()
        self.boundary()
        self.hero_state_check()
        self.hero_state_animation()
        self.draw_health_bar()
