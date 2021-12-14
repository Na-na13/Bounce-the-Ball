import sys
from random import randint
import pygame

from sprites.spriteball import Ball
from sprites.platform import Platform
from sprites.star import Star
from ui.end import End

WHITE = (255,255,255)
BLACK = (0,0,0)

class GameLoop:
    def __init__(self, window, clock):
        """Pelin pelisilmukka, joka pyörittää peliä

        Args:
            window (pygame display): peli-ikkuna
            clock (pygame clock): pelikello
        """
        self.window = window
        self.clock = clock
        self.right = False
        self.left = False
        self.jump = False
        self.gameover = False

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.collected_stars = 0
        self.init_sprites()

    def init_sprites(self):
        """Kaikkien pelin sprite-olioiden alustus:
            tasot, tähdet, pallo
        """
        pl1 = Platform(self.window.width/2+20,
                    self.window.height - self.window.margin - 100, 20, 100)
        pl2 = Platform(self.window.margin+2,
                self.window.height - self.window.margin-5, 5,
                self.window.width-2*self.window.margin)
        pl3 = Platform(pl1.rect.topleft[0]-210, pl1.rect.topleft[1]-100, 20, 200)
        pl4 = Platform(pl3.rect.topleft[0]-250, pl3.rect.topleft[1]-100, 20, 200)
        pl5 = Platform(pl4.rect.topright[0]+60, pl4.rect.topright[1]-120, 20, 100)
        pl6 = Platform(pl4.rect.topleft[0]-60, pl4.rect.topleft[1]-120, 20, 100)
        pl7 = Platform(pl1.rect.topright[0]+20, pl1.rect.topright[1]-100, 20, 180)
        pl8 = Platform(pl7.rect.topright[0]+60, pl7.rect.topright[1]-120, 20, 250)
        pl9 = Platform(pl5.rect.topright[0]+60, pl5.rect.topright[1]-120, 20, 250)
        pl10 = Platform(pl9.rect.topright[0]+60, pl9.rect.topright[1]-120,20,100)
        pl11 = Platform(pl10.rect.bottomright[0]+60, pl10.rect.bottomright[1]+100,20,80)
        pl12 = Platform(pl6.rect.topleft[0]-160, pl6.rect.topleft[1]-120, 20, 200)
        pl13 = Platform(pl12.rect.topright[0]+60,pl12.rect.topright[1]-120, 20, 200)
        self.ball = Ball(20,self.window.height,self.window.width,self.window.margin,self,pl2)
        self.stars.add(Star(self.window.width/2+70,self.window.height - self.window.margin - 230))
        self.platforms.add(pl1,pl2,pl3,pl4,pl5,pl6,pl7,pl8,pl9,pl10,pl11,pl12,pl13)
        self.all_sprites.add(self.platforms, self.stars)

    def new_game(self):
        """Uuden pelin alustaminen, muuttujat asetetaan alkutilaan, sprite.Groupit
            tyhjennetään, spritet alustetaan uudelleen ja pelisilmukka aloitetaan.
        """
        self.right = False
        self.left = False
        self.jump = False
        self.gameover = False

        self.all_sprites.empty()
        self.platforms.empty()
        self.stars.empty()
        self.collected_stars = 0

        self.init_sprites()
        self.loop()

    def loop(self):
        """Varsinainen pelisilmukka, joka pyörittää peliä. Kun muuttujan self.gameover
            arvoksi asetetaan False, pelisilmukka pysähtyy ja siirrytään lopetusikkunaan.
        """
        start = self.clock.clock_get_ticks()
        while not self.gameover:
            self.next_event()
            self.move_ball()
            self.check_star_collision()
            self.draw_display()
            self.clock.clock_tick(60)

        time = (self.clock.clock_get_ticks() - start)/1000
        end = End(self, time)
        end.run()

    def next_event(self):
        """Hakee seuraavan tapahtuman pygamen generoimasta tapahtumajonosta.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameover = True
                    self.new_game()
                if event.key == pygame.K_q:
                    sys.exit()
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
        """Tarkistaa tähtien keräämisen. Jos pallo osuu tähteen, tähti katoaa
            ja uusi tähti generoidaan satunnaiseen paikkaan pelialueella.
            Laskuri kasvaa yhdellä (jos laskurissa on yksi tähti, peli päättyy).
        """
        star_hit = pygame.sprite.spritecollide(self.ball,self.stars,True)
        if star_hit:
            star_hit[0].kill()
            self.collected_stars += 1
            while True:
                x = randint(self.window.margin + 20, self.window.width - self.window.margin -20)
                y = randint(self.window.margin + 20, self.window.height - self.window.margin -20)
                star = Star(x,y)
                self.stars.add(star)
                self.all_sprites.add(star)
                hit = pygame.sprite.spritecollide(star,self.platforms,False)
                if hit:
                    star.kill()
                    continue
                break
            if self.collected_stars == 3:
                self.gameover = True

    def draw_display(self):
        """Pallon liikkeiden päivittäminen, tähtien kerääminen ja peli-ikkunan piirtäminen
        """
        self.ball.update()
        self.check_star_collision()
        self.all_sprites.update()
        self.window.draw()
        self.all_sprites.draw(self.window.display)
        self.ball.draw(self.window.display)
        pygame.display.flip()
