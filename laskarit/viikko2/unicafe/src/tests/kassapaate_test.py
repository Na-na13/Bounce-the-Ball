import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti_vajaa = Maksukortti(200)

    def test_alustus_tehty_oikein(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat), (100000,0,0))

    def test_kateismaksu_riittaa_rahastus_oikein_edullinen(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual((self.kassapaate.kassassa_rahaa,takaisin),(100240,60))

    def test_kateismaksu_ei_riittaa_palautus_oikein_edullinen(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual((self.kassapaate.kassassa_rahaa,takaisin),(100000,150))

    def test_kateismaksu_riittaa_lounaiden_maara_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateismaksu_riittaa_rahastus_oikein_maukas(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(460)
        self.assertEqual((self.kassapaate.kassassa_rahaa,takaisin),(100400,60))
        
    def test_kateismaksu_ei_riittaa_palautus_oikein_maukas(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual((self.kassapaate.kassassa_rahaa,takaisin),(100000,150))

    def test_kateismaksu_riittaa_lounaiden_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_riittavasti_rahaa_edullinen(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),self.maksukortti.saldo),(True,760))

    def test_korttimaksu_riittaa_lounaiden_maara_kasvaa_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttimaksu_ei_riita_lounaiden_maara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vajaa)
        self.assertEqual(self.kassapaate.edulliset,0)
        
    def test_korttimaksu_ei_riita_kassan_rahamaara_ei_muutu_edullinen(self): 
        ret = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vajaa)
        self.assertEqual((self.kassapaate.kassassa_rahaa,ret),(100000,False))
    
    def test_korttimaksu_ei_riita_kortin_saldo_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vajaa)
        self.assertEqual(self.maksukortti_vajaa.saldo,200)

    def test_kortilla_riittavasti_rahaa_maukas(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),self.maksukortti.saldo),(True,600))

    def test_korttimaksu_riittaa_lounaiden_maara_kasvaa_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_ei_riita_lounaiden_maara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vajaa)
        self.assertEqual(self.kassapaate.maukkaat,0)
        
    def test_korttimaksu_ei_riita_kassan_rahamaara_ei_muutu_maukas(self): 
        ret = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vajaa)
        self.assertEqual((self.kassapaate.kassassa_rahaa,ret),(100000,False))

    def test_korttimaksu_ei_riita_kortin_saldo_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vajaa)
        self.assertEqual(self.maksukortti_vajaa.saldo,200)

    def test_kortilla_lataaminen_toimii_kun_summa_oikea(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual((self.kassapaate.kassassa_rahaa,self.maksukortti.saldo),(100500,1500))

    def test_kortilla_lataaminen_ei_toimi_kun_summa_vaara(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-10)
        self.assertEqual((self.kassapaate.kassassa_rahaa,self.maksukortti.saldo),(100000,1000))
