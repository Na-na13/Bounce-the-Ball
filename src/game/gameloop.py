import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

class GameLoop:
    def __init__(self, game):
        self.game = game

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
            self.display.fill(WHITE) 
            pygame.draw.rect(self.display, BLACK, (self.margin,self.margin
                            ,self.width-2*self.margin, self.heigth-2*self.margin),2) 
            pygame.display.flip()
