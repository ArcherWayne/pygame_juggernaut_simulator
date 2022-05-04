import pygame, sys, time
import setting
import hero, creep

# general setup
## pygame setup
pygame.init()
screen = pygame.display.set_mode(setting.window_size)

pygame.display.set_caption('juggernaut simulator')
pygame.display.set_icon(pygame.image.load('assets/blade game.png'))
background_surface = pygame.transform.scale(
    pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

## varibles setup
game_active = True

# class setup
# class = Class()

# group setup
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()


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

        if game_active:
            screen.fill(setting.WHITE)
            screen.blit(background_surface, background_rect)


        pygame.display.update()


if __name__ == "__main__":
    main()
