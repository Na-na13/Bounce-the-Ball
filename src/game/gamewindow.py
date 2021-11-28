import pygame
import gameloop

from ball import Ball

class GameWindow:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.height = pygame.display.get_window_size()[1]
        self.width = pygame.display.get_window_size()[0]
        self.margin = 20 # vaihda suhdelukuun näytön koon kanssa

if __name__ == "__main__":
    game = GameWindow()
    ball = Ball(20,game.height,game.width,game.margin)
    gameloop.GameLoop(game,ball)
