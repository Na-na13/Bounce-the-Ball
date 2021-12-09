import pygame
from gameloop import GameLoop

from gamewindow import GameWindow
from clock import Clock

def main():
    gamewindow = GameWindow()
    gameclock = Clock()
    gameloop = GameLoop(gamewindow, gameclock)

    pygame.init()
    gameloop.loop()

if __name__ == "__main__":
    main()
