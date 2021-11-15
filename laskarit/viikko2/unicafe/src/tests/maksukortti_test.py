import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahat_riittivat(self):
        message = "virhe: rahojen olisi pitänyt riittää"
        self.assertTrue(self.maksukortti.ota_rahaa(500),message)
    
    def test_rahat_eivat_riittaneet(self):
        message = "virhe: rahojen ei olisi pitänyt riittää"
        self.assertFalse(self.maksukortti.ota_rahaa(2000),message)
