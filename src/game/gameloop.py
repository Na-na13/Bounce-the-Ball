import pygame

from clock import Clock
from gamewindow import GameWindow
from sprites.spriteball import Ball
from sprites.platform import Platform
from sprites.star import Star

WHITE = (255,255,255)
BLACK = (0,0,0)

class GameLoop:
    def __init__(self, window, clock):
        self.window = window # GameWindow()
        self.right = False
        self.left = False
        self.jump = False
        self.clock = clock # Clock()

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.collected_stars = 0
        self.init_sprites()

    def init_sprites(self):
        pl1 = Platform(self.window.width/2+20,
                self.window.height - self.window.margin - 100, 20, 100)
        pl2 = Platform(self.window.margin+2,
                self.window.height - self.window.margin-5, 5,
                self.window.width-2*self.window.margin)
        self.ball = Ball(20,self.window.height,self.window.width,self.window.margin,self,pl2)
        self.stars.add(Star(self.window.width/2+70,self.window.height - self.window.margin - 230))
        #self.stars.add(Star(self.window.width/3,self.window.height-self.window.margin-150))
        self.platforms.add(pl1,pl2)
        self.all_sprites.add(self.platforms, self.stars)

    def loop(self):
        # start = self.clock.clock_get_ticks()
        while True:
            self.next_event()
            if self.is_moving():
                self.check_star_collision()
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
                if event.key == pygame.K_SPACE and self.jump is False:
                    self.jump = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False

    def is_moving(self):
        moves = [self.left,
                self.right,
                self.jump]

        if True in moves:
            return True
        return False

    def move_ball(self):
        if self.right:
            if not self.ball.move_right():
                self.right = False

        if self.left:
            if not self.ball.move_left():
                self.left = False

        if self.jump:    
            if not self.ball.jump():
                self.jump = False

    def check_star_collision(self):
        star_hit = pygame.sprite.spritecollide(self.ball,self.stars,True)
        if star_hit:
            star_hit[0].kill()    
            self.collected_stars += 1
            if self.collected_stars == 1:
                self.stars.add(Star(self.window.width/3,self.window.height-self.window.margin-150))
                self.all_sprites.add(self.stars)
            print(f"tähtiä kerätty: {self.collected_stars}")

    def draw_display(self):
        self.ball.update()
        self.check_star_collision()
        self.all_sprites.update()
        self.window.draw()
        self.all_sprites.draw(self.window.display)
        self.ball.draw(self.window.display)
        pygame.display.flip()

if __name__ == "__main__":
    window = GameWindow()
    clock = Clock()
    game = GameLoop(window, clock)
    game.loop()
