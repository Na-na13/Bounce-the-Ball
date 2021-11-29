# Bounce the Ball (ohjelmistotekniikka, harjoitustyö)  
Bounce the Ball on yksinkertainen tasohyppelypeli, jossa liikutetaan palloa läpi pelikentän kohti maalia keräten matkalla tähtiä, joista saa pisteitä
  
## Dokumentaatiot
[Tuntikirjanpito](https://github.com/Na-na13/Bounce-the-Ball/blob/master/dokumentaatiot/tuntikirjanpito.md)  
[Määrittelydokumentti](https://github.com/Na-na13/Bounce-the-Ball/blob/master/dokumentaatiot/maarittelydokumentti.md)
    
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
poetry run invoke coverage_report
```

Koodin laadun tarkistus:
```bash
poetry run invoke pylint
```
