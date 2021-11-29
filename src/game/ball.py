import pygame

RED = (255,0,0)

class Ball:
    def __init__(self, radius, height, width, margin):
        pygame.init()
        self.ball_radius = radius # vaihda suhdelukuun näytön koon kanssa
        self.ball_x = width/2
        self.ball_y = height - margin - radius - 2
        #self.height = height
        #self.width = width
        #self.margin = margin
        # self.move_right = False
        # self.move_left = False

    def draw_ball(self, surface):
        pygame.draw.circle(surface, RED, (self.ball_x,self.ball_y), self.ball_radius)

    #def move_ball_right(self):
    #    if self.move_right:
    #        if self.ball_x >= self.width - self.margin - 7 - self.ball_radius:
    #            self.move_right = False
    #        else:
    #           self.ball_x += 10

    #def move_ball_left(self):
    #    if self.move_left:
    #        if self.ball_x <= self.margin + 7 + self.ball_radius:
    #            self.move_left = False
    #        else:
    #            self.ball_x -= 10

    #def is_moving(self):
    #    if self.move_ball_left == True or self.move_ball_left == True:
    #        return True

    #def jump_ball(self):
    #    pass
