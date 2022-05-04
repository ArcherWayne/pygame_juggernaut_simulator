class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super(Player, self).__init__(groups)

        # image
        self.image = pygame.Surface(player_size)
        self.image.fill('#345678')

        # position
        self.rect = self.image.get_rect(midtop=(300, 700))
        self.old_rect = self.rect.copy()

        # movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 280


    def update(self, dt):
        self.old_rect = self.rect.copy()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)

