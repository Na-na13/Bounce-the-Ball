import pygame

RED = (255,0,0)
WHITE = (255,255,255)

class Ball (pygame.sprite.Sprite):
    def __init__(self, radius, height, width, margin, game, ground):
        super().__init__()

        self.ball_radius = radius # vaihda suhdelukuun näytön koon kanssa
        self.height = height
        self.width = width
        self.margin = margin
        self.game = game
        self.current_pl = ground

        self.image = pygame.Surface((radius*2,radius*2))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.current_pl.rect.midtop
        self.max_jumpheight = 150
        self.vertical = 0

    def draw(self,surface):
        pygame.draw.circle(surface, RED, (self.rect.center), self.ball_radius)

    def move_right(self):
        if self.rect.right >= self.width - self.margin - 7:
            return False
        self.rect.x += 10
        if self.rect.midbottom[0] > self.current_pl.rect.topright[0]:
            self.vertical = -10
        return True

    def move_left(self):
        if self.rect.left < self.margin + 7:
            return False
        self.rect.x -= 10
        if self.rect.midbottom[0] < self.current_pl.rect.topleft[0]:
            self.vertical = -10
        return True

    def jump(self):
        self.rect.y += 1
        hit = pygame.sprite.spritecollide(self, self.game.platforms,False)
        self.rect.y -= 1
        if hit:
            self.current_pl = hit[0]
            self.vertical = 10
            return True
        return False

    def update(self):
        hit = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hit and self.rect.bottom >= hit[0].rect.top:
            if self.vertical == 10:
                self.vertical = -10
            elif self.vertical == -10:
                self.rect.y = hit[0].rect.top - self.ball_radius*2
                self.vertical = 0
                self.current_pl = hit[0]
        if self.rect.bottom < self.current_pl.rect.top - self.max_jumpheight:
            self.vertical = -10
        self.rect.y -= self.vertical
