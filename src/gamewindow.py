import pygame

from settings import *

class GameWindow:
    def __init__(self):
        """Peli-ikkuna, luodaan fullscreen-tilassa
        """
        pygame.init()

        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.height = pygame.display.get_window_size()[1]
        self.width = pygame.display.get_window_size()[0]

    def draw(self):
        """Asettaa peli-ikkunan pohjavärin valkoiseksi ja piirtää peli-ikkunan
            ympärille pelialueen rajat marginaalin päähän kuvaruudun reunoista.
        """
        self.display.fill(WHITE)
        pygame.draw.rect(self.display, BLACK, (MARGIN, MARGIN,
                        self.width - 2 * MARGIN, self.height- 2 * MARGIN), LINE)
