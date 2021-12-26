import pygame

from settings import *

class Ball (pygame.sprite.Sprite):
    def __init__(self, height, width, game, ground):
        """Pallo-sprite, joka on pelin liikuteltava hahmo.

        Args:
            radius (int): pallon säde
            height (int): peli-ikkunan korkeus
            width (int): peli-ikkunan leveys
            margin (int): peli-ikkunan marginaali
            game (gameloop): pelisilmukka
            ground (sprite): alin taso-sprite, jolta peli alkaa
        """
        super().__init__()

        self.height = height
        self.width = width
        self.game = game
        self.current_pl = ground

        self.image = pygame.Surface((BALLRADIUS * 2, BALLRADIUS * 2))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.current_pl.rect.midtop
        self.vertical = 0

    def draw(self,surface):
        """Pallon piirtäminen peli-ikkunaan

        Args:
            surface (pygame.Surface): peli-ikkuna, jolle piirto tapahtuu
        """
        pygame.draw.circle(surface, RED, (self.rect.center), BALLRADIUS)

    def move_right(self):
        """Tarkistaa, onko pallon liikkuminen oikealle sallittua.
            Liikkuminen rajoitettu peli-ikkunaan.
            Jos pallo liikkuu tason oikein reunan yli, pallon liike muutetaan
            alaspäin suuntautuvaksi.

        Returns:
            boolean: True, jos liikkuminen sallittua, False, jos osutaan seinään
        """
        if self.rect.right >= self.width - MARGIN - 7:
            return False
        self.rect.x += 10
        if self.rect.midbottom[0] > self.current_pl.rect.topright[0]:
            self.vertical = -10
        return True

    def move_left(self):
        """Tarkistaa, onko pallon liikkuminen vasemmalle sallittua.
            Liikkuminen rajoitettu peli-ikkunaan.
            Jos pallo liikkuu tason vasemman reunan yli, pallon liike muutetaan
            alaspäin suuntautuvaksi.

        Returns:
            boolean: True, jos liikkuminen sallittua, False, jos osutaan seinään
        """
        if self.rect.left < MARGIN + 7:
            return False
        self.rect.x -= 10
        if self.rect.midbottom[0] < self.current_pl.rect.topleft[0]:
            self.vertical = -10
        return True

    def jump(self):
        """Tarkistaa, onko pallolla hyppääminen sallittua.
            Hyppääminen mahdollista vain, jos pallo on tason päällä.

        Returns:
            boolean: True, jos pallo on tason päällä, muuten False
        """
        self.rect.y += 1
        hit = pygame.sprite.spritecollide(self, self.game.platforms,False)
        self.rect.y -= 1
        if hit:
            self.current_pl = hit[0]
            self.vertical = 10
            return True
        return False

    def update(self):
        """Päivittää pallon liikkeet. Jos pallo osuu alhaaltapäin yläpuolella
            olevaan tasoon, liike muutetaan alaspäin suuntautuvaksi. Jos pallo
            osuu ylhäältäpäin alapuolella olevaan tasoon, pallo jää tason päälle.
            Jos saavutetaan maksimi hyppykorkeuden, liike muutetaan alaspäin
            suuntautuvaksi. Pallo ei voi hypätä peli-ikkunan ulkopuolelle.
            (Bugi: joissakin tapauksissa pallo voi hypätä yläpuolelta tason läpi)
        """
        hit = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hit and self.rect.bottom >= hit[0].rect.top:
            if self.vertical == 10:
                self.vertical = -10
            elif self.vertical == -10:
                self.rect.y = hit[0].rect.top - BALLRADIUS * 2
                self.vertical = 0
                self.current_pl = hit[0]
        if self.rect.top <= MARGIN + LINE:
            self.vertical = -10
        if self.rect.bottom < self.current_pl.rect.top - MAXJUMPHEIGHT:
            self.vertical = -10
        self.rect.y -= self.vertical
