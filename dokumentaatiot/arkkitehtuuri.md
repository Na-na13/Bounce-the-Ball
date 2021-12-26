## Arkkitehtuurikuvaus  
### Pelin rakenne
![kaaviokuva](https://user-images.githubusercontent.com/81189092/147420919-f9980eae-0975-4270-8adc-a54a2b0800d7.jpg)
  
Pelin rakenne noudattaa ylläolevaa kaaviokuvaa. Pelin aloitusvalikoluokalle *Start* annetaan parametreina luokan *Clock* olio sekä luokan *GameWindow* olio. Näiden parametrien avulla saadaan pelisilmukan muodostava luokka *Gameloop* suoritukseen. Toimiakseen oikein luokka *Gameloop* tarvitsee lisäksi luokkien *Ball*, *Platform* ja *Star* olioita. Pelin päätyttyä luokan *GameLoop* suoritus päättyy ja siirrytään käsittelemään lopetusvalikon luomaa luokkaa *End*.
  
### Valikot
Peli sisältää on kaksi erillistä valikkoa:  
1. [aloitusvalikko](https://github.com/Na-na13/Bounce-the-Ball/blob/master/src/ui/start.py)  
2. [lopetusvalikko](https://github.com/Na-na13/Bounce-the-Ball/blob/master/src/ui/end.py)  
    
Kumpikin valikko on toteutettu omana luokkanaan. Valikon painikkeita painamalla saadaan esille eri näkymiä, kuten pelin ohjeistus, 'Best Times'-lista sekä itse pelinäkymä. Muut näkymät, paitsi pelinäkymä, luodaan luokkien alustuksen yhteydessä ja niiden näkyvyyttä ja toiminnallisuutta säädellää sen mukaan, mitä painikkeita pelaaja klikkailee. Kun peli käynnistetään, aloitusvalikko tulee ensimmäisenä näkyviin. Klikkaamalla 'Play'-painiketta [alustetaan pelisilmukka](https://github.com/Na-na13/Bounce-the-Ball/blob/3b95a03a59151019f7705a607b794c0e2a22b0c9/src/ui/start.py#L90) ja näkymä vaihtuu pelitilaan. Pelitilasta palataan lopetusvalikkoon [pelin päätyttyä](https://github.com/Na-na13/Bounce-the-Ball/blob/3b95a03a59151019f7705a607b794c0e2a22b0c9/src/gameloop.py#L88). Kummallakin valikolla on oma silmukkansa, joka vastaa valikon toimintojen suorituksesta eli käytännössä mitä tapahtuu mistäkin painikkeesta.  
  
### Tiedon pysyväistallennus  
Lopetusvaliko hallinnoi peliaikojen tallentamista [tekstitiedostoon](https://github.com/Na-na13/Bounce-the-Ball/blob/master/src/high_score.txt), johon peliaika ja pelaajan nimi tallennetaan csv-tyylisesti. Peliajat ovat tiedostossa nopeusjärjestyksessä ja tiedostosta löytyy kymmenen parasta tallennettua peliaikaa. Lopetusvalikko antaa pelaajalle mahdollisuuden tallentaa ajan tiedostoon, jos se on nopeampi kuin tiedoston listan viimeinen aika. Aloitusvalikossa on myös mahdollisuus valita tämän tiedoston listan tarkastelu, jolloin pelaajalle näytetään sen hetkinen kymmenen parhaan ajan lista nopeusjärjestyksessä.

### Pallon liikuttaminen pelissä
Pelin päätoiminnallisuudet muodostuvat pallolla liikkuminen sekä pallolla hyppääminen. Hyppäämistä sekä vasemalle liikkumista on kuvattu alla olevilla sekvenssikaavioilla. Oikealle liikkumisen periaate on sama kuin vasemmalle liikkumisen.    
![seq_jump](https://user-images.githubusercontent.com/81189092/145106670-4384fe01-a93f-4380-b582-4ce27be0678c.jpg)  
Pelaaja painaa välilyöntinäppäintä, jolloin *GameLoop* alustaa pallon hyppäämistä varten asettamalla [hyppäämisen sallituksi](https://github.com/Na-na13/Bounce-the-Ball/blob/3b95a03a59151019f7705a607b794c0e2a22b0c9/src/gameloop.py#L106). Tämän jälkeen hypyn salliminen varmistetaan siten, että luokka *Ball* varmistaa, että pallo on [tasanteen päällä](https://github.com/Na-na13/Bounce-the-Ball/blob/3b95a03a59151019f7705a607b794c0e2a22b0c9/src/sprites/spriteball.py#L77), jolloin hyppääminen on sallittua. Pallon liikesuunta muutetaan ylöspäin ja tämä tieto palautetaan luokalle *GameLoop*. Nyt *Gameloop* voi päivittää pallon liikkeen ylöspäin, jolloin pelaaja näkee pallon hyppäävän.  

![seq_left](https://user-images.githubusercontent.com/81189092/147421580-e6601872-a899-464c-9766-4911f90e866e.jpg)  
Pelaaja painaa vasenta nuolinäppäintä, jolloin *GameLoop* alustaa pallon [liikkumaan vasemmalle](https://github.com/Na-na13/Bounce-the-Ball/blob/3b95a03a59151019f7705a607b794c0e2a22b0c9/src/gameloop.py#L102). Tämän jälkeen liikkeen salliminen varmistetaan siten, että luokka *Ball* tarkistaa, että [pallo pysyy pelialueella](https://github.com/Na-na13/Bounce-the-Ball/blob/3b95a03a59151019f7705a607b794c0e2a22b0c9/src/sprites/spriteball.py#L62). Pallon liikesuunta muutetaan vasemmalle ja tieto palautetaan luokalle *GameLoop*. Nyt *GameLoop* voi päivittää pallon liikesuunnan vasemmalle ja pelaaja näkee pallon liikkuvan vasemmalle.
   
#### Bugeja pallon liikuttamisessa
Peliin jäi pieniä bugi, jonka takia joissain tapauksissa pallo pystyy menemään tasanteen läpi yläkautta ja siten siis tippumaan peli-ikkunan ulkopuolelle pelialueen alareunasta. Lisäksi pallolla hyppiminen voisi olla sulavampaa, mutta hyppytoiminnallisuus kuitenkin toimii jokseenkin hyvin.
