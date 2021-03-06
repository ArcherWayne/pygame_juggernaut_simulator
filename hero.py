import pygame
import math
import random
from hero_skill import HeroSkill
from debug import debug
from clip import clip
from setting import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, name, health, movement_speed, damage, attacking_distance, foreswing, backswing):
        super(Hero, self).__init__(groups)
        # attributes -------------------------------------------------------------------------------- #
        self.name = name
        self.health = health
        self.max_health = self.health
        self.health_percentage = self.health/self.max_health
        self.movement_speed = movement_speed
        self.damage = damage
        self.attacking_distance = attacking_distance
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

        # idle_animation
        idle_image = pygame.image.load(
            'assets/hero/hero_idle_animation.png').convert_alpha()
        idle_animation_frame_1_right = pygame.transform.scale(
            clip(idle_image, 0, 0, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        idle_animation_frame_2_right = pygame.transform.scale(
            clip(idle_image, 0, 96, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        idle_animation_frame_3_right = pygame.transform.scale(
            clip(idle_image, 0, 192, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        idle_animation_frame_1_left = pygame.transform.flip(
            idle_animation_frame_1_right, 1, 0)
        idle_animation_frame_2_left = pygame.transform.flip(
            idle_animation_frame_2_right, 1, 0)
        idle_animation_frame_3_left = pygame.transform.flip(
            idle_animation_frame_3_right, 1, 0)
        self.idle_animation_list_right = [
            idle_animation_frame_1_right, idle_animation_frame_2_right, idle_animation_frame_3_right, idle_animation_frame_2_right]
        self.idle_animation_list_left = [
            idle_animation_frame_1_left, idle_animation_frame_2_left, idle_animation_frame_3_left, idle_animation_frame_2_left]

        # walking_animation
        walking_image = pygame.image.load(
            'assets/hero/hero_walking_animation.png').convert_alpha()
        walking_animation_frame_1_right = pygame.transform.scale(
            clip(walking_image, 0, 0, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        walking_animation_frame_2_right = pygame.transform.scale(
            clip(walking_image, 0, 96, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        walking_animation_frame_3_right = pygame.transform.scale(
            clip(walking_image, 0, 192, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        walking_animation_frame_4_right = pygame.transform.scale(
            clip(walking_image, 0, 288, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        walking_animation_frame_1_left = pygame.transform.flip(
            walking_animation_frame_1_right, 1, 0)
        walking_animation_frame_2_left = pygame.transform.flip(
            walking_animation_frame_2_right, 1, 0)
        walking_animation_frame_3_left = pygame.transform.flip(
            walking_animation_frame_3_right, 1, 0)
        walking_animation_frame_4_left = pygame.transform.flip(
            walking_animation_frame_4_right, 1, 0)
        self.walking_animation_list_right = [walking_animation_frame_1_right, walking_animation_frame_2_right,\
            walking_animation_frame_3_right, walking_animation_frame_4_right]
        self.walking_animation_list_left = [walking_animation_frame_1_left, walking_animation_frame_2_left, \
            walking_animation_frame_3_left, walking_animation_frame_4_left]

        # attack animation
        attack_image = pygame.image.load(
            'assets/hero/hero_attack_animation.png').convert_alpha()
        attack_animation_frame_1_right = pygame.transform.scale(
            clip(attack_image, 0, 0, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        attack_animation_frame_2_right = pygame.transform.scale(
            clip(attack_image, 0, 96, 96, 96), (HERO_WIDTH, HERO_HEIGHT))
        attack_animation_frame_1_left = pygame.transform.flip(
            attack_animation_frame_1_right, 1, 0)
        attack_animation_frame_2_left = pygame.transform.flip(
            attack_animation_frame_2_right, 1, 0)
        self.attack_animation_list_right = [attack_animation_frame_1_right, attack_animation_frame_2_right]
        self.attack_animation_list_left = [attack_animation_frame_1_left, attack_animation_frame_2_left]

        # init animation
        self.image = idle_animation_frame_1_right
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        # self.collision_rect = pygame.Rect(0, 0, HERO_WIDTH/2, HERO_HEIGHT/2)
        # self.old_collision_rect = self.collision_rect.copy()

        # movement ---------------------------------------------------------------------------------- #
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.old_rect = self.rect.copy()  # old_rect是用来检测碰撞的一部分, 不是dt中的一部分
        self.facing_direction = 0  # = 0 面向左边 = 1 面向右边

        # sound effect ------------------------------------------------------------------------------ #
        self.attack_sound_tuple = (pygame.mixer.Sound('assets/sound/Juggernaut_attack1.mp3'), \
            pygame.mixer.Sound('assets/sound/Juggernaut_attack2.mp3'), pygame.mixer.Sound('assets/sound/Juggernaut_attack2.mp3'))
        # self.attack_sound.set_volume(0.5)

        # state check ------------------------------------------------------------------------------- #
        self.idle_state = 1
        self.moving_state = 0
        self.attacking_state = 0
        self.skill_1_state = 0
        self.skill_2_state = 0
        self.skill_3_state = 0
        self.skill_4_state = 0
        self.state_check_list = [self.idle_state, self.moving_state, self.attacking_state,
                            self.skill_1_state, self.skill_2_state, self.skill_3_state, self.skill_4_state]

        # varibles init ----------------------------------------------------------------------------- #
        # self.creep = creep
        self.attack_target = 0
        # self.flag_moving = 0
        self.target_pos = (0, 0)
        self.idle_animation_index = 0
        self.walking_animation_index = 0
        self.attack_animation_index = 0

    def get_dt(self, dt):
        self.dt = dt

    def keyboard_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.moving_state = 0
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.moving_state = 0
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.moving_state = 0
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.moving_state = 0
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
            self.moving_state = 1

    def mouse_movement(self):
        if self.moving_state:
            self.direction.y = self.target_pos[1] - self.rect.midbottom[1]
            self.direction.x = self.target_pos[0] - self.rect.midbottom[0]

            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.pos.x += self.direction.x * self.movement_speed * self.dt
            self.rect.x = round(self.pos.x)
            self.pos.y += self.direction.y * self.movement_speed * self.dt
            self.rect.y = round(self.pos.y)

        if self.rect.midbottom == self.target_pos:
            self.moving_state = 0

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

    def hero_facing_direction(self):
        if self.old_rect.x < self.rect.x:
            self.facing_direction = 1
        elif self.old_rect.x > self.rect.x:
            self.facing_direction = 0

    def hero_state_check(self):
        # update hero state
        # check idle and movement state
        if self.attacking_state == 1:
            self.idle_state = 0
            self.moving_state = 0
        else:
            if self.old_rect.x != self.rect.x or self.old_rect.y != self.rect.y:
                self.idle_state = 0
                self.moving_state = 1
            else:
                self.idle_state = 1
                self.moving_state = 0

        self.state_check_list = [self.idle_state, self.moving_state, self.attacking_state,
                                 self.skill_1_state, self.skill_2_state, self.skill_3_state, self.skill_4_state]

    def hero_state_animation(self):
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
            self.walking_animation_index += 1/10
            if self.facing_direction == 1:  # facing right
                if self.walking_animation_index >= len(self.walking_animation_list_right):
                    self.walking_animation_index = 0
                self.image = self.walking_animation_list_right[int(
                    self.walking_animation_index)]
            elif self.facing_direction ==0: # facing left
                # self.walking_animation_index += 1/30
                if self.walking_animation_index >= len(self.walking_animation_list_left):
                    self.walking_animation_index = 0
                self.image = self.walking_animation_list_left[int(
                    self.walking_animation_index)]
        if self.state_check_list[2]:
            self.attack_animation_index += 1/10
            if 0.9 < self.attack_animation_index < 1.0:
                self.hero_attack()
            # if self.facing_direction == 1: # facing right
            if self.attack_target.rect.x > self.pos.x:
                if self.attack_animation_index >= len(self.attack_animation_list_right):
                    self.attack_animation_index = 0
                    self.attacking_state = 0
                    self.facing_direction = 1
                self.image = self.attack_animation_list_right[int(
                    self.attack_animation_index)]

            # elif self.facing_direction == 0: # facing left
            elif self.attack_target.rect.x < self.pos.x:
                if self.attack_animation_index >= len(self.attack_animation_list_left):
                    self.attack_animation_index = 0
                    self.attacking_state = 0
                    self.facing_direction = 0
                self.image = self.attack_animation_list_left[int(
                    self.attack_animation_index)]
        if self.state_check_list[3]:
            pass
        if self.state_check_list[4]:
            pass
        if self.state_check_list[5]:
            pass
        if self.state_check_list[6]:
            pass

    def draw_health_bar(self):
        self.health_percentage = self.health/self.max_health
        health_bar_background = pygame.Rect(
            self.rect.midtop[0] - 42, self.rect.midtop[1] - 22, 84, 12)
        health_bar_content = pygame.Rect(
            self.rect.midtop[0] - 40, self.rect.midtop[1] - 20, round(80 * self.health_percentage), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def hero_init_attack(self, creep):
        self.attack_target = creep
        self.distance_when_attacking = math.sqrt(math.pow((self.rect.midbottom[0]-creep.rect.midbottom[0]),2)+\
            math.pow((self.rect.midbottom[1]-creep.rect.midbottom[1]),2))

        if self.distance_when_attacking > self.attacking_distance:
            # print('小兵太远!')
            self.init_mouse_movement(creep.rect.midbottom)
        elif self.distance_when_attacking <= self.attacking_distance:
            self.attacking_state = 1

    def hero_attack(self):
        self.attack_target.creep_attacked(self.damage)
        self.attack_sound_tuple[random.randint(0,2)].play()

    def hero_use_skill(self, pressed_key):
        match pressed_key:
            case 1:
                HeroSkill().blade_fury()
            case 2:
                HeroSkill().healing_ward()
            case 3:
                HeroSkill().blade_dance()
            case 4:
                HeroSkill().swiftslash()

    def update(self):
        self.old_rect = self.rect.copy()

        self.keyboard_movement()
        self.mouse_movement()
        self.boundary()
        self.hero_facing_direction()
        self.draw_health_bar()
        self.hero_state_check()
        self.hero_state_animation()


# reference ------------------------------------------------------------------------------------------ #

# class 类1:
#     def __init__(self, 类2) -> None:
#         self.类2 = 类2

#     def 调用类2方法(self):
#         self.类2.方法()

# class 类2:
#     def 方法(self)

# def collision_hero_creep_enemy():
#     c_list = pygame.sprite.spritecollide(hero.sprite, creep_enemy_group, False)
#     if c_list:
#         hero.sprite.health_reduce(c_list[0].damage)
#         c_list[0].health_reduce(hero.sprite.damage)
#         print(hero.sprite.health)
#         print(c_list[0].health)