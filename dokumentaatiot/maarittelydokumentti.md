## Bounce the Ball
**ohjelmointikieli: python**
  
**dokumentaatiokieli: suomi**  
  
*Bounce the Ball* on idealtaan yksinkertainen hyppely-peli. Pelin ideana on kerätä pelin liikuteltavalla hahmolla punaisella pallolla mahdollisimman nopeasti seitsemän satunnaisiin paikkoihin ilmestyvää tähteä osumalla niihin pallolla. Pelialueella on 12 tasannetta, joiden päälle pallolla voi hypätä. Kun seitsemän tähteä on kerätty, peli päättyy. Jos peliaika on ollut tarpeeksi nopea (nopeampi kuin 'Best Times'-listan viimeinen aika) pelaajalle tarjotaan mahdollisuutta tallettaa oma aikansa 'Best Times'-listalle. Jos taas peliaika on ollut hitaampi kuin listan viimeinen aika, talletusmahdollisuutta ei pelaajalle tarjota.
  
### Syötteet  
  
Palloa liikutellaan vasemmalle ja oikealle vastaavilla nuolinäppäimillä ja pallolla hypätään välilyöntinäppäimellä. Hypyn aikana pystyy samalla liikkumaan vasemmalle tai oikealle. Tasanteiden läpi ei pysty hyppimään, vaan jokaiselle tasanteelle pääsee vain hyppäämällä sen päädystä sen päälle. Tasanteet on sijoiteltu niin, että hypyn epäonnistuessa on mahdollista tippua alaspäin. Tippumisen aikana on myös mahdollista liikkua vasemmalle ja oikealle samalla tavoin kuin hypynkin aikana.  

### Tähtien kerääminen   
  
Tähtiä kerätään osumalla pallolla tähteen. Ensimmäinen tähti ilmestyy aina samaan kohtaan pelialuetta. Kun tähti on kerätty, seuraava tähti ilmestyy jne., kunnes seitsemän tähteä on kerätty, jolloin peli päättyy. Ensimmäisen tähden jälkeen tähdet ilmestyvät satunnaisiin paikkoihin pelialueella, joten satunnaisuuden takia pelin vaikeustaso ei välttämättä ole aina sama.
   
### Lisäideoita 
#### Pelialueen laajentaminen 
  
Pelialue liikkuu sivuttais- tai pitkittäissuuntaisesti ('side-scrolling'), kun pallolla saavutetaan tietty kohta peli-ikkunan x-/y-akselilla, jolloin tähtiä voisi ilmestyä aina pallon edessä olevalle alueelle.
  
#### Esteet/hidasteet  
  
Pelikentällä on erilaisia pallon etenemistä hidastavia esteitä, kuten ylhäältä tippuvia partikkeleita, joiden alle ei saa jäädä, sekä tasoissa olevia piikkiosuuksia, joihin ei saa osua. Jos esteistä ei selviydy, pallo puhkeaa ja pelin joutuu aloittamaan alusta  
  
#### Tasanteelta tippuminen  
  
Jos tasanteelta tippuu liian pitkän matkan alaspäin, pallo puhkeaa ja joutuu aloittamaan alusta  
   
### Edistyminen
- [x] pallon liikuttaminen vasemmalle ja oikealle nuolinäppäimillä
- [x] pallolla hyppääminen välilyöntinäppäimellä
- [x] pallolla hyppääminen tasanteille
- [x] tähtien kerääminen
- [x] ajanotto
- [x] aloitusikkuna
- [x] lopetusikkuna
- [x] Best Times -lista
