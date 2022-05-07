            screen.fill(WHITE)
            screen.blit(background_surface, background_rect)
            all_sprites.update()
            all_sprites.draw(screen)

            debug(mouse_pos, 10, 10)

            pygame.display.update()