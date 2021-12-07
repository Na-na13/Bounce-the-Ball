import pygame
import os

BLACK = (0,0,0)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Star (pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join(img_folder, "star.png")).convert_alpha()
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
