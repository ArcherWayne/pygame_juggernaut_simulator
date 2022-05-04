import pygame, sys, time
import setting


# general setup
pygame.init()
screen = pygame.display.set_mode(window_size)
game_active = True


# class setup


# group setup
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
# class = Class()


def main():
    last_time = time.time()
    
    while True:

        # delta time
        dt = time.time() - last_time
        last_time = time.time()

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

        # screen.fill('#123456')
        # all_sprites.update(dt)
        # all_sprites.draw(screen)
        # pygame.display.update()

if __name__ == "__main__":
    main()
