import pygame

window_size = (1400, 800)
WIN_WIDTH = window_size[0]
WIN_HEIGHT = window_size[1]
screen = pygame.display.set_mode(window_size)

FPS = 60

# hero stats
# __init__(self, name, health, movement_speed, damage, forswing, backswing, flag_moving)
HERO_HEIGHT = 60
HERO_WIDTH = 60
HERO_HEALTH = 600
HERO_MOVEMENT_SPEED = 200
HERO_DAMAGE = 50
HERO_FORESWING = 0.1
HERO_BACKSWING = 0.2


# creep stats
# __init__(self, health, movement_speed, damage, forswing, backswing)
CREEP_HEIGHT = 60
CREEP_WIDTH = 60
CREEP_HEALTH = 50
CREEP_CIT_HEALTH = HERO_DAMAGE - 1
CREEP_MOVEMENT_SPEED = 80
CREEP_DAMAGE = 5
CREEP_FORESWING = 0.2
CREEP_BACKSWING = 0.2


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)