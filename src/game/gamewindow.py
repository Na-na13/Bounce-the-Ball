import pygame

from ball import Ball
from gameloop import GameLoop
#from map import Platform

class GameWindow:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.height = pygame.display.get_window_size()[1]
        self.width = pygame.display.get_window_size()[0]
        self.margin = 20 # vaihda suhdelukuun näytön koon kanssa
        #self.platforms = pygame.sprite.Group()
        #self.all_sprites = pygame.sprite.Group()

        #self.init_sprites()

    #def init_sprites(self):
    #    self.platforms.add(Platform(self.width/2+20, self.height - self.margin - 70, 20, 100))
    #    self.all_sprites.add(Ball(20,self.height,self.width,self.margin))
    #    self.all_sprites.add(self.platforms)

    #def draw_sprites(self):
    #    self.all_sprites.draw(self.display)


if __name__ == "__main__":
    game = GameWindow()
    ball = Ball(20,game.height,game.width,game.margin)
    loop = GameLoop(game,ball)
    loop.loop()
