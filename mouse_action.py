import pygame
from hero import Hero

def mouse_action(mouse_pos, mouse_click_pos, mouse_click_button, hero):
    if mouse_click_button == 1:
        pass

    if mouse_click_button == 2:
        pass

    if mouse_click_button == 3:
        hero.init_mouse_movement(mouse_click_pos)