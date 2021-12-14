import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)

class GameWindow:
    def __init__(self):
        """Peli-ikkuna, luodaan fullscreen-tilassa
        """
        pygame.init()

        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.height = pygame.display.get_window_size()[1]
        self.width = pygame.display.get_window_size()[0]
        self.margin = 20 # vaihda suhdelukuun näytön koon kanssa

    def draw(self):
        """Asettaa peli-ikkunan pohjavärin valkoiseksi ja piirtää peli-ikkunan
            ympärille pelialueen rajat marginaalin päähän kuvaruudun reunoista.
        """
        self.display.fill(WHITE)
        pygame.draw.rect(self.display, BLACK, (self.margin, self.margin
                        ,self.width-2*self.margin, self.height-2*self.margin),2)
