import unittest
from varasto import Varasto

#Muutos 12-4

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus(self):
        # Paulan lisäys
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        # Paulan lisäys
        varasto = Varasto(10,-1)
        self.assertEqual(varasto.saldo, 0)

    def test_positiivinen_alkusaldo(self):
        # Paulan lisäys
        varasto = Varasto(10,3)
        self.assertEqual(varasto.saldo, 3)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_onnistu(self):
        # Paulan lisäys
        self.varasto.lisaa_varastoon(-100)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_liian_lisays_palauttaa_maksimin(self):
        # Paulan lisäys
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)


    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_ottaminen_ei_onnistu(self):
        # Paulan lisäys
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_kaiken_ottaminen(self):
        # Paulan lisäys
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str(self):
        # Paulan lisäys
        varasto = Varasto(10, 2)
        expected_string = "saldo = 2, vielä tilaa 8"
        self.assertEqual(str(varasto), expected_string)
