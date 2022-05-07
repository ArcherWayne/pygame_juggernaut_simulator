import pygame, sys, time
from setting import *
from creep import Creep
from hero import Hero
from debug import debug


# general setup --------------------------------------------------------------------------------------------- #
## pygame setup
pygame.init()

pygame.display.set_caption('juggernaut simulator')
pygame.display.set_icon(pygame.image.load('assets/blade game.png'))
background_surface = pygame.transform.scale(
    pygame.image.load('assets/background/ground.png').convert(), (WIN_WIDTH, WIN_HEIGHT))
background_rect = background_surface.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

## varibles setup
game_active = True

# class setup
# class = Class()


# group setup ----------------------------------------------------------------------------------------------- # 
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
hero = Hero(all_sprites, 'Juggernaut', HERO_HEALTH, HERO_MOVEMENT_SPEED, HERO_DAMAGE, HERO_FORESWING, HERO_BACKSWING) 
# groups, name, health, movement_speed, damage, foreswing, backswing

# mouse control --------------------------------------------------------------------------------------------- # 
mouse_pos = (0, 0)



# main ------------------------------------------------------------------------------------------------------ # 


def main():
    last_time = time.time()
    while True:
        

        # delta time    ------------------------------------------------------------------------------------- #
        dt = time.time() - last_time
        last_time = time.time()

        # event loop    ------------------------------------------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

        mouse_pos = pygame.mouse.get_pos()

        if game_active:
            

            # draw stuff    --------------------------------------------------------------------------------- #
            screen.fill(WHITE)
            screen.blit(background_surface, background_rect)
            all_sprites.update(dt)
            all_sprites.draw(screen)

            debug(mouse_pos, 10, 10)

            pygame.display.update()


if __name__ == "__main__":
    main()
