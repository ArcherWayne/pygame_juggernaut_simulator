import pygame
from hero import Hero
from creep import Creep


def mouse_action(mouse_pos, mouse_click_pos, mouse_click_button, hero, creep_group, cursor):
    if mouse_click_button == 1:
        pass

    if mouse_click_button == 2:
        pass

    if mouse_click_button == 3:
        if pygame.sprite.spritecollide(cursor, creep_group, False):
            for creep in creep_group.sprites():
                if pygame.Rect.collidepoint(creep.rect, mouse_click_pos):
                    hero.hero_attack(creep)
        else:
            hero.init_mouse_movement(mouse_click_pos)




        # if spritecollide(sprite, group, dokill, collided = None) -> Sprite_list

        # for creep in creep_group.sprites():
        #     if pygame.Rect.collidepoint(creep.rect, mouse_click_pos):
        #         hero.hero_attack(creep)

        # hero.init_mouse_movement(mouse_click_pos)