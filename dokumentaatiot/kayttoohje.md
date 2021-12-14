## Käyttöohje
### Pelin käynnistäminen
Pelin käynnistäminen tapahtuu aloittamalla riippuvuuksien asentaminen komentorivin komennolla
```bash
poetry install
```
Tämän jälkeen pelin voi käynnistää komennolla
```bash
poetry run invoke start
```
### Aloittaminen  
Kun peli on käynnistetty, ensimmäisenä aukeaa kuvan mukainen pelin aloitusikkuna.    
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/146051256-4dbf6c9d-253a-474b-b075-90ab34fa585c.png" />
</p>  
Ikkunassa näkyvillä on valikko, josta pelaaja pystyy hiirellä klikkaamalla valitsemaan haluaako pelata, katsoa pelin ohjeistuksen, katsoa pelin Best times -listan (ei toimi vielä) tai lopettaa pelaaminen.  
  
### Pelaaminen  
Kun pelaaja on valinnut aloitusvalikosta halutuksi toiminnoksi pelaamisen, peli siirtyy varsinaiseen pelitilaan ja avautuu kuvan mukainen näkymä.  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/146051493-1a5a1f86-275e-4740-bc2d-663b6f3900ad.png" />
</p>  
Pelin aloitusasetelmassa pelin ohjattava objekti punainen pallo on keskellä alinta tasoa. Palloa pystyy liikuttelemaan nuolinäppäimillä ja hyppäämään välilyöntinäppäimellä. Pallolla pystyy hyppäämään tasojen päälle ja keräämään tähtiä osumalla niihin. Kun tähteen osuu, se katoaa ja uusi tähti tulee esiin satunnaisesti generoituu paikkaan pelialueella. Tarkoituksena (määrittelydokumentista poikete) on kerätä 10 tähteä mahdollisimman nopeasti. 
  
### Lopettaminen  
Kun 10 tähteä on kerätty (tällä hetkellä kun tähtiä on kerätty kaksi), avautuu kuvan mukainen lopetusikkuna:  
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/146053475-60cb695f-708a-46fa-9242-327fa39f40a6.png" />
</p> 
Ikkunan valikossa on näkyvissä peliin käytetty aika. Jos pelaaja haluaa tallettaa aikansa, syötetään nimimerkki tekstisyöttökenttään ja painetaan 'Save'. Nimimerkki ja peliaika tallennetaan Best times -listaan, jos se yltää kymmenen parhaan ajan joukkoo (ei toimi toistaiseksi). Valikossa on myös mahdollista valita uuden pelin aloitus tai lopettaa pelaaminen.
