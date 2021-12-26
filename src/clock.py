import pygame

class Clock:
    def __init__(self):
        """Pelikello, joka määrittää pelin päivitystahtia
        """
        self.clock = pygame.time.Clock()

    def clock_tick(self, fps):
        """Kutsutaan aina kerran pelisilmukan iteraation aikana.
            Rajoittaa pelin nopeutta näyttämällä maksimissaan
            argumentin fps määrän frameja sekunnissa.

        Args:
            fps (int): kuinka monta kertaa framea näytetään sekunnissa
        """
        self.clock.tick(fps)

    def clock_get_ticks(self):
        """Palauttaa millisekunteina kauan kutsusta 'pygame.init()'
            on kulunut
        """
        return pygame.time.get_ticks()
