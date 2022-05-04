import pygame
import setting

class Hero(pygame.sprite.Sprite):
    def __init__(self, name, health, movement_speed, damage, foreswing, backswing, flag_moving):
        super(Hero, self).__init__()
        self.name = name
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.foreswing = foreswing
        self.backswing = backswing
        self.flag_moving = flag_moving

        self.hero_surface = pygame.transform.scale(
            pygame.image.load('assets/graphics/heroes/hero 45.png').convert_alpha(), (HERO_HEIGHT, HERO_WIDTH)
        )
        # 以下两行只能名字叫做image和rect, 这是pygame定义的draw函数中规定的 更新: 并不是
        self.image = self.hero_surface
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGTH / 2))

    def mouse_right_click(self):
        pass
        # 语法: 检验右键是否与某个小兵像素碰撞
        # 若没碰撞 则调用移动函数到右键点击的位置
        # 若碰撞 则先移动到与小兵一定距离 然后调用攻击函数

    def movement(self):
        pass
        # # 每帧移动0.1秒, 更新后又重新定位为原来的位置, 所以一定要数值比1 大(能否为比1大的小数呢)
        # # self.rect.y += 1
        # # self.rect.x += 1
        # mouse_click = pygame.mouse.get_pressed()
        # mouse_pos = pygame.mouse.get_pos()

        # global target_pos

        # if mouse_click[2] and mouse_pos != self.rect.midbottom:
        #     target_pos = mouse_pos
        #     self.flag_moving = 1
        # elif mouse_click[2] and mouse_pos == self.rect.midbottom:
        #     self.flag_moving = 0

        # if self.flag_moving:
        #     y_distance = self.rect.midbottom[1] - target_pos[1]
        #     x_distance = self.rect.midbottom[0] - target_pos[0]

        #     y_speed = int(math.sqrt(
        #         math.pow(self.movement_speed, 2) / (math.pow((x_distance / y_distance), 2) + 1)
        #     )) if y_distance != 0 else 0
        #     x_speed = int(math.sqrt(
        #         math.pow(self.movement_speed, 2) / (math.pow((y_distance / x_distance), 2) + 1)
        #     )) if x_distance != 0 else 0

        #     if y_distance < 0:
        #         self.rect.y += y_speed
        #     elif y_distance > 0:
        #         self.rect.y -= y_speed
        #     if x_distance < 0:
        #         self.rect.x += x_speed
        #     elif x_distance > 0:
        #         self.rect.x -= x_speed
        #     # if abs(self.rect.x-target_pos[0]) < x_speed or \
        #     #         abs(self.rect.y-target_pos[1]) < y_speed:
        #     if math.sqrt(math.pow(self.rect.midbottom[0] - target_pos[0], 2) + math.pow(
        #             self.rect.midbottom[1] - target_pos[1], 2)) < self.movement_speed:
        #         self.rect.x = target_pos[0] - HERO_WIDTH / 2
        #         self.rect.y = target_pos[1] - HERO_HEIGHT
        #     if self.rect.midbottom == target_pos:
        #         self.flag_moving = 0

    def attack(self):
        pass

    def animation(self):
        if self.flag_moving == 1:
            pass

    def draw_health_bar(self):
        health_bar_background = pygame.Rect(self.rect.midtop[0] - 42, self.rect.midtop[1] - 22, 84, 12)
        health_bar_content = pygame.Rect(self.rect.midtop[0] - 40, self.rect.midtop[1] - 20,
                                         80 * (self.health / HERO_HEALTH), 8)
        pygame.draw.rect(screen, BLACK, health_bar_background)
        pygame.draw.rect(screen, RED, health_bar_content)

    def health_reduce(self, creep_damage):
        self.health -= creep_damage

    def update(self):
        self.draw_health_bar()
        self.movement()