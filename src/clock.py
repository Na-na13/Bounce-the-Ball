import pygame

from time import time

class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def clock_tick(self, fps):
        self.clock.tick(fps)

    #def clock_get_ticks(self):
    #    return pygame.time.get_ticks()

    def get_time(self):
        return time()
