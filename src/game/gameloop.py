import pygame

from clock import Clock

WHITE = (255,255,255)
BLACK = (0,0,0)

class GameLoop:
    def __init__(self, game, ball):
        self.game = game
        self.ball = ball
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.max_jumpheight = 150
        self.clock = Clock()
        self.start = self.clock.clock_get_ticks()

        self.loop()
        

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_LEFT:
                        self.left = True
                    if event.key == pygame.K_RIGHT:
                        self.right = True
                    if event.key == pygame.K_SPACE and self.up == False:
                        if self.down == False:
                            self.up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left = False
                    if event.key == pygame.K_RIGHT:
                        self.right = False
            if self.right:
                if self.ball.ball_x >= self.game.width - self.game.margin - 7 - self.ball.ball_radius:
                    self.right = False
                else:
                    self.ball.ball_x += 10
            if self.left:
                if self.ball.ball_x <= self.game.margin + 7 + self.ball.ball_radius:
                    self.left = False
                else:
                    self.ball.ball_x -= 10

            if self.up:
                if self.ball.ball_y <= self.game.height - self.game.margin - self.ball.ball_radius - self.max_jumpheight:
                    self.up = False
                    self.down = True
                    
                else:
                    self.ball.ball_y -= 10

            if self.down:
                if self.ball.ball_y == self.game.height - self.game.margin - self.ball.ball_radius - 2:
                    self.down = False
                else:
                    self.ball.ball_y += 10

            self.game.display.fill(WHITE) 
            pygame.draw.rect(self.game.display, BLACK, (self.game.margin,self.game.margin
                            ,self.game.width-2*self.game.margin, self.game.height-2*self.game.margin),2) 
            self.ball.draw_ball(self.game.display)
            pygame.display.flip()
            self.clock.clock_tick(60)
