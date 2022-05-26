import pygame
from setting import *

class Cursor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load('assets/cursor.png').convert_alpha(), (CURSOR_WIDTH, CURSOR_HEIGHT))
        self.rect = self.image.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

    def get_pos(self, mouse_pos):
        self.rect.topleft = mouse_pos

    def update(self):
        pass
