import pygame
import gameloop
from ball import Ball

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class BounceTheBall:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.heigth = pygame.display.get_window_size()[1]
        self.width = pygame.display.get_window_size()[0]
        self.margin = 20 # vaihda suhdelukuun näytön koon kanssa
        self.ball_x = self.width/2
        self.ball_y = self.heigth-self.margin-20-2
        self.ball_radius = 20 # vaihda suhdelukuun näytön koon kanssa
        self.ball = pygame.draw.circle(self.display, RED, (self.width/2, self.heigth-self.margin-2),40)
        
        #self.ball = Ball()
        #self.ball.draw_ball(self.display)
        #gameloop.GameLoop.loop(self)
        
        clock = pygame.time.Clock()

        right = False
        left = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left = True
                    if event.key == pygame.K_RIGHT:
                        right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        left = False
                    if event.key == pygame.K_RIGHT:
                        right = False
            if right:
                if self.ball_x >= self.width - self.margin - 7 - self.ball_radius:
                    right = False
                else:
                    self.ball_x += 10
            if left:
                if self.ball_x <= self.margin + 7 + self.ball_radius:
                    left = False
                else:
                    self.ball_x -= 10
            self.display.fill(WHITE) 
            pygame.draw.rect(self.display, BLACK, (self.margin,self.margin
                            ,self.width-2*self.margin, self.heigth-2*self.margin),2) 
            pygame.draw.circle(self.display, RED, (self.ball_x, self.ball_y),self.ball_radius)
            #self.ball.draw_ball(self.display)
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    BounceTheBall()
