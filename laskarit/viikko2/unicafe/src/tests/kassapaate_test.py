import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti_vajaa = Maksukortti(200)

    def test_alustus_tehty_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_kateismaksu_riittaa_edullinen(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240) 
        self.assertEqual(takaisin,60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateismaksu_ei_riitta_edullinen(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(takaisin, 150)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateismaksu_riittaa_rahastus_oikein_maukas(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(460)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400) 
        self.assertEqual(takaisin,60)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kateismaksu_ei_riitta_maukas(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(takaisin, 150)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_riittavasti_rahaa_edullinen(self):
        ret = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(ret, True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttimaksu_ei_riita_edullinen(self):
        ret = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_vajaa)
        self.assertEqual(ret, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.maksukortti_vajaa.saldo, 200)

    def test_kortilla_riittavasti_rahaa_maukas(self):
        ret = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(ret, True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_ei_riita_maukas(self):
        ret = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_vajaa)
        self.assertEqual(ret, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti_vajaa.saldo, 200)

    def test_kortilla_lataaminen_toimii_kun_summa_oikea(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_kortilla_lataaminen_ei_toimi_kun_summa_vaara(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)
