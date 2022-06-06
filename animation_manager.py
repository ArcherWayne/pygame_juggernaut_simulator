import pygame
from clip import clip
from debug import debug
from setting import *


class AnimationManager(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # animation dict
        self.animation_dict = {'blood_animation': 0, 'some_animation': 0}

        # loading blood animation
        blood_animation_image = pygame.image.load('assets/blood_animation.png').convert_alpha()
        self.blood_animation_image_list = []
        for x in range(0, 384, 32):
            self.blood_animation_image_list.append(
                pygame.transform.scale(clip(blood_animation_image, 0, x, 32, 32), (CREEP_WIDTH, CREEP_HEIGHT)))

        # animation index
        self.blood_animation_index = 0

    def init_animation(self, animation, play_location):
        # if animation == 'blood_animation':
        #     self.blood_animation()
        self.play_location = play_location
        for animation_name in self.animation_dict.keys():
            if animation == animation_name:
                self.animation_dict[animation_name] = 1

    def blood_animation(self):
        blood_animation_play_location = (0, 0)
        if self.animation_dict['blood_animation'] == 1:
            blood_animation_play_location = self.play_location
            self.blood_animation_index += 1
            if self.blood_animation_index >= len(self.blood_animation_image_list):
                self.blood_animation_index = 0
                self.animation_dict['blood_animation'] = 0
            screen.blit(self.blood_animation_image_list[int(self.blood_animation_index)], (blood_animation_play_location[0] - CREEP_WIDTH / 2, blood_animation_play_location[1] - CREEP_HEIGHT / 2))
            # FIXME : 使用更新image的方法?
            # HACK : self.image 的显示方法是通过pygame.sprite.Sprite()类的方法实现的, 所以 暂时没想到更好的方法

    def update(self):
        self.blood_animation()
        # debug(self.animation_dict)
