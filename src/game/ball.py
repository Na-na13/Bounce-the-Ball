import pygame

RED = (255,0,0)
WHITE = (255,255,255)

class Ball:
    def __init__(self, radius, height, width, margin):
        pygame.init()
        self.ball_radius = radius # vaihda suhdelukuun näytön koon kanssa
        self.ball_x = width/2
        self.ball_y = height - margin - radius - 2
        self.height = height
        self.width = width
        self.margin = margin
        self.max_jumpheight = 150

    def draw_ball(self, surface):
        pygame.draw.circle(surface, RED, (self.ball_x,self.ball_y), self.ball_radius)

    def move_right(self):
        if self.ball_x >= self.width - self.margin - 7 - self.ball_radius:
            return False
        self.ball_x += 10
        return True

    def move_left(self):
        if self.ball_x <= self.margin + 7 + self.ball_radius:
            return False
        self.ball_x -= 10
        return True

    def move_up(self):
        if self.ball_y <= self.height - self.margin - self.ball_radius - self.max_jumpheight:
            return False
        self.ball_y -= 10
        return True

    def move_down(self):
        if self.ball_y == self.height - self.margin - self.ball_radius - 2:
            return False
        self.ball_y += 10
        return True
