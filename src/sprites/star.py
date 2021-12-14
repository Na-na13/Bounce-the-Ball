import os
import pygame

game_folder = os.path.split(os.path.dirname(__file__))[0]
img_folder = os.path.join(game_folder,"img")

class Star (pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Star-sprite on peli kerättävä objekti

        Args:
            x (int): tähden vasemman yläkulman x-koordinaatti
            y (int): tähden vasemman yläkulman y-koordinaatti
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join(img_folder, "star2.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
