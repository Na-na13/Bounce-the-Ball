# Bounce the Ball (ohjelmistotekniikka, harjoitustyö)  
Bounce the Ball on yksinkertainen hyppelypeli, jossa pallolla kerätään 10 pelikentälle satunnaisesti generoituihin paikkoihin ilmestyvää tähteä mahdollisimman nopeasti.
  
## Dokumentaatiot
[Tuntikirjanpito](https://github.com/Na-na13/Bounce-the-Ball/blob/master/dokumentaatiot/tuntikirjanpito.md)  
[Määrittelydokumentti](https://github.com/Na-na13/Bounce-the-Ball/blob/master/dokumentaatiot/maarittelydokumentti.md)  
[Käyttöohje](https://github.com/Na-na13/Bounce-the-Ball/blob/master/dokumentaatiot/kayttoohje.md)  
[Arkkitehtuuri](https://github.com/Na-na13/Bounce-the-Ball/blob/master/dokumentaatiot/arkkitehtuuri.md)
  
## Julkaistut versiot
[Viikon 5 versio](https://github.com/Na-na13/Bounce-the-Ball/releases/tag/viikko5)  
[Viikko 6 versio](https://github.com/Na-na13/Bounce-the-Ball/releases/tag/viikko6)
    
## Pelin käynnistäminen
1. Asenna rippuvuudet
```bash
poetry install
```
2. Käynnista peli
```bash
poetry run invoke start
```
  
## Testaus
Testien suorittaminen:
```bash
poetry run invoke test
```
Testikattavuus:
```bash
poetry run invoke coverage-report
```
Koodin laadun tarkistus:
```bash
poetry run invoke pylint
```
