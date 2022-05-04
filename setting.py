import pygame

window_size = (1400, 800)
WIN_WIDTH = window_size[0]
WIN_HEIGTH = window_size[1]

FPS = 60

# hero stats
# __init__(self, name, health, movement_speed, damage, forswing, backswing, flag_moving)
HERO_HEIGHT = 60
HERO_WIDTH = 60
HERO_HEALTH = 120
HERO_MOVEMENT_SPEED = 4
HERO_DAMAGE = 16
HERO_FORESWING = 0.1
HERO_BACKSWING = 0.2


# creep stats
# __init__(self, health, movement_speed, damage, forswing, backswing)
CREEP_HEIGHT = 60
CREEP_WIDTH = 60
CREEP_HEALTH = 50
CREEP_CIT_HEALTH = HERO_DAMAGE - 1
CREEP_MOVEMENT_SPEED = 2
CREEP_DAMAGE = 5
CREEP_FORESWING = 0.2
CREEP_BACKSWING = 0.2


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)