import pygame

window_size = (1400, 800)

FPS = 60
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))

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

# tower stats
TOWER_HEIGHT = 285
TOWER_WIDTH = 205
TOWER_HEALTH = 500
TOWER_DAMAGE = 10

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
