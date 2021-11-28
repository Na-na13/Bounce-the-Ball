import pygame

RED = (255,0,0)

class Ball:
    def __init__(self, radius, heigth, width, margin):
        self.ball_radius = radius # vaihda suhdelukuun näytön koon kanssa
        self.ball_x = width/2
        self.ball_y = heigth - margin - self.radius - 2
        
    def draw_ball(self, surface):
        pygame.draw.circle(surface, RED, self.ball_x,self.ball_y,self.ball_radius)
