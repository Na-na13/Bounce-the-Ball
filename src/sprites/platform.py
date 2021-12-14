import pygame

BLACK = (0,0,0)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        """Platform-spritet ovat suorakulmion muotoisia
            tasoja, joita pitkin pallolla hypitään ylöspäin
            kohti maalia.

        Args:
            x (int): tason vasemman yläkulman x-koodrinaatti
            y (int): tason vasemman yläkulman y-koordinaatti
            height (int): tason korkeus
            width (int): tason leveys
        """
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
