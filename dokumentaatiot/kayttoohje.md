## Käyttöohje
Lataan ensin pelin lähdekoodi valitsemalla viimeisen [releasen](https://github.com/Na-na13/Bounce-the-Ball/releases) *Assets*-pudotusvalikon alta *Source Code*.  
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
Kun peli on käynnistetty, ensimmäisenä aukeaa kuvan mukainen pelin aloitusvalikko.    
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/147419669-4b351e3a-7108-4b5d-8c27-fbd5e72c85da.png" />
</p>  
Pelaaja pystyy hiirellä klikkaamalla valitsemaan valikosta haluaako pelata, katsoa pelin ohjeistuksen, katsoa pelin Best Times -listan tai lopettaa pelaaminen.
 
### Ohjeistus  
Kun pelaaja valitsee aloitusvalikosta 'Instructions', avautuu pelaajalle uuteen tekstilaatikkoon pelin ohjeistus lyhyesti.
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/147419850-8cf65ac8-fdbc-46b2-a905-d7ba5c8ceb3c.png" />
</p>  
Klikkaamalla ohjeistuksen alapuolella olevaa 'Return'-painiketta, näkymä palaa takaisin aloitusvalikkoon.
  
### Best Times
Kun pelaaja valitsee aloituvalikosta 'Best Times', avautuu pelaajalle uuteen tekstilaatikkoon sen hetkinen lista kymmenestä parhaasta listaan tallennetusta peliajasta.
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/147419978-5c2e8a0b-76ab-4058-82ca-74c68c4e63aa.png" />
</p>
Jos listaan ei ole tallennettu yhtään peliaikaa, on oletusnäkymä kuvan mukainen. Läpi pelatun pelin jälkeen pelaajalle annetaan mahdollisuus tallettaa listaan oman peliaikansa, jos se on parempi kuin listan viimeinen aika. Tällöin listan viimeinen aika poistetaan ja uusi aika tallennetaan listaan järjestyksessä omaan paikkaansa. Klikkaamalla listan alapuolella olevaa 'Return'-painiketta, näkymä palaa takaisin aloitusvalikkoon.
  
### Pelaaminen  
Kun pelaaja on valinnut aloitusvalikosta halutuksi toiminnoksi pelaamisen, peli siirtyy varsinaiseen pelitilaan ja avautuu kuvan mukainen näkymä.  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/146051493-1a5a1f86-275e-4740-bc2d-663b6f3900ad.png" />
</p>  
Pelin aloitusasetelmassa pelin ohjattava objekti punainen pallo on keskellä alinta tasoa. Palloa pystyy liikuttelemaan nuolinäppäimillä ja hyppäämään välilyöntinäppäimellä. Pallolla pystyy hyppäämään tasojen päälle ja keräämään tähtiä osumalla niihin. Kun tähteen osuu, se katoaa ja uusi tähti tulee esiin satunnaisesti generoituu paikkaan pelialueella. Tarkoituksena on kerätä 7 tähteä mahdollisimman nopeasti. Kun nämä seitsemän tähteä on kerätty, peli päättyy.
  
### Lopettaminen  
Kun 7 tähteä on kerätty, peli päättyy ja lopetusvalikko avautuu. Valikon ulkonäköön vaikuttaa se, miten nopeasti peli on pelattu läpi. Jo aiemminkin mainittiin, jos pelin pelaa nopeammin kuin 'Best Times'-listalla oleva viimeinen aika, pelaajalle annetaan mahdollisuus tallettaa aika listalle. Muulloin mahdollisuutta ei anneta.  
  
#### Talletusmahdollisuus  
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/147420340-1d51603b-df49-43b3-806d-bbbca20647b5.png" />
</p>
Valikon tekstilaatikossa on näkyvissä peliin käytetty aika. Jos pelaaja haluaa tallettaa aikansa, syötetään nimimerkki tekstisyöttökenttään ja painetaan 'Save'. Nimimerkki ja peliaika tallennetaan Best times -listaan, jos se yltää kymmenen parhaan ajan joukkoo. 'Save'-painikkeen painamisen jälkeen näkyviin tulee päivitetty 'Best Times'-lista. Valikossa on myös mahdollista valita uuden pelin aloitus tai lopettaa pelaaminen.
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/147420385-060dc169-75e5-4ec2-9fe4-a1a2efcf3d87.png" />
</p>     
  
#### Ei talletusmahdollisuutta   
Jos peliaika ei ole nopeampi kuin listan viimeinen aika, pelaajalle ei anneta mahdollisuutta tallettaa peliaikaa listalle ja lopetusvalikko näyttää kuvan mukaiselta. Peliaika näytetään pelaajalle ja pelaaja voi valita, haluaako pelata uudelleen vai lopettaa pelaamisen.     
<p align="center">
  <img src="https://user-images.githubusercontent.com/81189092/147420470-b16d4fd9-9e74-4d79-a783-bae9ab1e1a67.png" />
</p>  
