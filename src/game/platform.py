import pygame

BLACK = (0,0,0)

class Platform (pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
