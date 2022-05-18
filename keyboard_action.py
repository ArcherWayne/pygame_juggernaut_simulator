import pygame
from hero import Hero
from hero_skill import *

# w 119 s 115 a 97 d 100

def keyboard_action(keyboard_down_button, hero):
    if keyboard_down_button == 49:
        # key 1 is pressed
        hero.hero_use_skill(1)

    if keyboard_down_button == 50:
        # key 2 is pressed
        hero.hero_use_skill(2)

    if keyboard_down_button == 51:
        # key 3 is pressed
        hero.hero_use_skill(3)

    if keyboard_down_button == 52:
        # key 4 is pressed
        hero.hero_use_skill(4)