import pygame
from hero import Hero

def mouse_action(mouse_pos, mouse_click_pos, mouse_click_button, hero):
    # mouse_pos_ma = mouse_pos
    # mouse_click_pos_ma = mouse_click_pos
    # mouse_click_button_ma = mouse_click_button
    # dt_ma = dt

    if mouse_click_button == 3:
        hero.init_mouse_movement(mouse_click_pos)

    