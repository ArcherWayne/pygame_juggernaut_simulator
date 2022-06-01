import pygame, sys, time, random
from setting import *
from creep import Creep
from hero import Hero
from debug import debug
from mouse_action import mouse_action
from keyboard_action import keyboard_action
from cursor import Cursor


# general setup --------------------------------------------------------------------------------------------- #
## pygame setup
pygame.init()
pygame.display.set_caption('juggernaut simulator')
pygame.display.set_icon(pygame.image.load('assets/blade game.png'))
background_surface = pygame.transform.scale(
    pygame.image.load('assets/background/map.png').convert(), (WIN_WIDTH, WIN_HEIGHT))
background_rect = background_surface.get_rect(
    center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()

## varibles setup
game_active = True
pygame.mouse.set_visible(False)


# class setup
# class = Class()
# group setup ----------------------------------------------------------------------------------------------- #
# all_sprites = pygame.sprite.Group()
# collision_sprites = pygame.sprite.Group()
cursor_group = pygame.sprite.GroupSingle()
cursor = Cursor(cursor_group)
hero_group = pygame.sprite.GroupSingle()
creep_group = pygame.sprite.Group()
hero = Hero(hero_group, 'Juggernaut', HERO_HEALTH,
            HERO_MOVEMENT_SPEED, HERO_DAMAGE, HERO_ATTACKINGDISTANCE, HERO_FORESWING, HERO_BACKSWING)

for i in range(3):
    creep_group.add(Creep(creep_group, CREEP_HEALTH, CREEP_MOVEMENT_SPEED, \
        CREEP_DAMAGE, (random.randint(200, 1200), random.randint(200, 600)), hero))

creep_enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(creep_enemy_timer, 3000)

# main ------------------------------------------------------------------------------------------------------ #
def main():
    last_time = time.time()

    # mouse control init ------------------------------------------------------------------------------------ #
    mouse_pos = (0, 0)
    mouse_click_pos = (0, 0)
    mouse_click_button = 0

    # keyboard control init --------------------------------------------------------------------------------- #
    keyboard_down_button = 0

    while True:
        # event loop    ------------------------------------------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                cursor.get_pos(mouse_pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_pos = event.pos
                mouse_click_button = event.button
                mouse_action(mouse_pos, mouse_click_pos, mouse_click_button, hero, creep_group, cursor)

            if event.type == pygame.KEYDOWN:
                keyboard_down_button = event.key
                keyboard_action(keyboard_down_button, hero)

            if event.type == creep_enemy_timer:
                creep_group.add(Creep(creep_group, CREEP_HEALTH, CREEP_MOVEMENT_SPEED, \
                    CREEP_DAMAGE, (random.randint(200, 1200), random.randint(200, 600)), hero))

        clock.tick(FPS)

        # delta time    ------------------------------------------------------------------------------------- #
        dt = time.time() - last_time
        hero.get_dt(dt)
        for creep in creep_group.sprites(): # Group.sprites() 加上括号才是返回groups中包含sprites的列表, 没有括号就是Group的方法
            creep.get_dt(dt)
        last_time = time.time()


        if game_active:
            # draw stuff    --------------------------------------------------------------------------------- #
            screen.fill(WHITE)
            screen.blit(background_surface, background_rect)
            creep_group.update()
            creep_group.draw(screen)
            hero_group.update()
            hero_group.draw(screen)
            cursor_group.update()
            cursor_group.draw(screen)

            # debug goes behind here !!! -------------------------------------------------------------------- #
            debug(creep_group.sprites())
            debug(int(1/dt), info_name='fps', y=30)


        pygame.display.update()


if __name__ == "__main__":
    main()
