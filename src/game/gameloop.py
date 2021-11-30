import pygame

from clock import Clock
#from map import Platform

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
        self.clock = Clock()

    def loop(self):
        # start = self.clock.clock_get_ticks()
        while True:
            self.next_event()
            if self.is_moving():
                self.move_ball()

            self.draw_display()
            self.clock.clock_tick(60)

    def next_event(self):
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
                if event.key == pygame.K_SPACE and self.up is False:
                    if self.down is False:
                        self.up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False

    def is_moving(self):
        moves = [self.left,
                self.right,
                self.up,
                self.down]

        if True in moves:
            return True
        else:
            return False

    def move_ball(self):
        if self.right:
            if not self.ball.move_right():
                self.right = False

        if self.left:
            if not self.ball.move_left():
                self.left = False

        if self.up:
            if not self.ball.move_up():
                self.up = False
                self.down = True
        
        if self.down:
            if not self.ball.move_down():
                self.down = False


    def draw_display(self):
        self.game.display.fill(WHITE)
        pygame.draw.rect(self.game.display, BLACK, (self.game.margin,self.game.margin
                        ,self.game.width-2*self.game.margin, self.game.height-2*self.game.margin),2)
        self.ball.draw_ball(self.game.display)
        #self.game.draw_sprites()
        pygame.display.flip()
