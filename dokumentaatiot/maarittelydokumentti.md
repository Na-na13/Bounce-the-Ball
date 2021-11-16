## Bounce the Ball
**ohjelmointikieli: python**
  
**dokumentaatiokieli: suomi**  
  
*Bounce the Ball* on idealtaan yksinkertainen tasohyppely-tyylinen peli. Pelin liikuteltava hahmo on punainen pallo, jolla hypitään tasanteita pitkin ylöspäin kohti maalia samalla keräten tähtiä. Mitä nopeammin saapuu maaliin ja mitä enemmän tähtiä matkalla kerää, sitä enemmän pisteitä saa. Pelissä kerätyt pisteet tallennetaan pelaajanimellä tiedostoon/tietokantaan, josta voidaan palauttaa high score-lista. 
  
### Syötteet  
  
Palloa liikutellaan vasemmalle ja oikealle vastaavilla nuolinäppäimillä ja pallolla hypätään välilyöntinäppäimellä. Hypyn aikana pystyy samalla liikkumaan vasemmalle tai oikealle. Tasanteiden läpi ei pysty hyppimään, vaan jokaiselle tasanteelle pääsee vain hyppäämällä sen päädystä sen päälle. Tasanteet on sijoiteltu niin, että hypyn epäonnistuessa on mahdollista tippua alaspäin. Tippumisen aikana on myös mahdollista liikkua vasemmalle ja oikealle samalla tavoin kuin hypynkin aikana.  
  
### Pisteiden kerääminen  
  
Pelissä on tarkoitus kerätä pelikentältä löytyviä tähtiä, jotka on sijoiteltu matkan varrelle, toiset helpompiin ja toiset haastavampiin paikkoihin. Tähden saa kerättyä osumalla pallolla tähteen. Jokaisesta tähdestä saa saman verran pisteitä. Pisteitä saa myös nopeudesta eli mitä nopeammin pallolla pääsee maaliin, sitä enemmän pisteitä saa

### Lisäideoita  
  
#### Esteet/hidasteet  
  
Pelikentällä on erilaisia pallon etenemistä hidastavia esteitä, kuten ylhäältä tippuvia partikkeleita, joiden alle ei saa jäädä, sekä tasoissa olevia piikkiosuuksia, joihin ei saa osua. Jos esteistä ei selviydy, pallo puhkeaa ja pelin joutuu aloittamaan alusta  
  
#### Tasanteelta tippuminen  
  
Jos tasanteelta tippuu liian pitkän matkan alaspäin, pallo puhkeaa ja joutuu aloittamaan alusta  
