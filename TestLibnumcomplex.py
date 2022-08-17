import unittest
import Libnumcomplex as lnc
import math


class TestCplxOperations(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(lnc.suma((2, 3), (3, 5)), (5, 8))

    def test_resta(self):
        self.assertEqual(lnc.resta((2, 3), (3, 5)), (-1, -2))

    def test_multiplicaion(self):
        self.assertEqual(lnc.multiplicacion((2, 3), (3, 5)), (-9, 19))

    def test_division(self):
        self.assertEqual(lnc.division((2, 3), (3, 5)), (21/34, 19/34))

    def test_modulo(self):
        self.assertEqual(lnc.modulo(2, 3), math.sqrt(13))

    def test_conjugado(self):
        self.assertEqual(lnc.conjugado(2, 3), (2, -3))

    def test_polar(self):
        self.assertEqual(lnc.polar(4, 3), (5, math.atan2(3, 4)))

    def test_cartesiano(self):
        self.assertEqual(lnc.cartesiano(5, math.atan2(3, 4)), (4, 3))

    def test_fase(self):
        self.assertEqual(lnc.fase(4, 3), math.atan2(3, 4))


if __name__ == '__main__':
    unittest.main()
