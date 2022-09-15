import unittest
import Libnumcomplex as lnc
import math
from fractions import Fraction


class TestCplxOperations(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(lnc.suma((2, 3), (3, 5)), (5, 8))

    def test_resta(self):
        self.assertEqual(lnc.resta((2, 3), (3, 5)), (-1, -2))

    def test_multiplicaion(self):
        self.assertEqual(lnc.multiplicacion((2, 3), (3, 5)), (-9, 19))

    def test_division(self):
        self.assertEqual(lnc.division((2, 3), (3, 5)), (21 / 34, 19 / 34))

    def test_modulo(self):
        self.assertEqual(lnc.modulo(2, 3), math.sqrt(13))

    def test_conjugado(self):
        self.assertEqual(lnc.conjugado((2, 3)), (2, -3))

    def test_polar(self):
        self.assertEqual(lnc.polar(4, 3), (5, math.atan2(3, 4)))

    def test_cartesiano(self):
        self.assertEqual(lnc.cartesiano(5, math.atan2(3, 4)), (4, 3))

    def test_fase(self):
        self.assertEqual(lnc.fase(4, 3), math.atan2(3, 4))

    def test_sumvector(self):
        V1 = [[[1, 2]], [[2, 3]], [[3, 4]], [[4, 5]]]
        V2 = [[[2, 4]], [[4, 6]], [[8, 10]], [[12, 14]]]
        rt = [[(3, 6)], [(6, 9)], [(11, 14)], [(16, 19)]]
        self.assertEqual(lnc.sumavectores(V1, V2), rt)


    def test_restavector(self):
        V1 = [[[1, 2]], [[2, 3]], [[3, 4]], [[4, 5]]]
        V2 = [[[2, 4]], [[4, 6]], [[8, 10]], [[12, 14]]]
        rt = [[(-1, -2)], [(-2, -3)], [(-5, -6)], [(-8, -9)]]
        self.assertEqual(lnc.restavectores(V1, V2), rt)


    def test_inversovector(self):
        V = [[[1, 2]], [[2, 3]], [[3, 4]], [[4, 5]]]
        rt = [[(-1, -2)], [(-2, -3)], [(-3, -4)], [(-4, -5)]]
        self.assertEqual(lnc.inversovector(V), rt)

    def test_multescalatvector(self):
        V = [[[2, 4]], [[4, 6]], [[8, 10]], [[12, 14]]]
        rt = [[(8, 6)], [(14, 8)], [(26, 12)], [(38, 16)]]
        self.assertEqual(lnc.multescalarvector((2, -1), V), rt)

    def test_sumamatrices(self):
        m1 = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        m2 = [
            [[2, 1], [3, 3], [1, 5]],
            [[2, 2], [3, 3], [5, 2]],
            [[1, 5], [2, 6], [7, 2]]
        ]
        rt = [[(3, 3), (5, 6), (2, 8)], [(6, 7), (8, 9), (11, 9)], [(3, 6), (7, 11), (11, 4)]]
        self.assertEqual(lnc.sumamatrices(m1, m2), rt)

    def test_inversomatriz(self):
        m = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        rt = [[(-1, -2), (-2, -3), (-1, -3)], [(-4, -5), (-5, -6), (-6, -7)], [(-2, -1), (-5, -5), (-4, -2)]]
        self.assertEqual(lnc.inversomatriz(m), rt)

    def test_multescalarmatriz(self):
        m = [
            [[2, 1], [3, 3], [1, 5]],
            [[2, 2], [3, 3], [5, 2]],
            [[1, 5], [2, 6], [7, 2]]
        ]
        rt = [[(5, 0), (9, 3), (7, 9)], [(6, 2), (9, 3), (12, -1)], [(7, 9), (10, 10), (16, -3)]]
        self.assertEqual(lnc.multescalarmatriz((2, -1), m), rt)

    def test_traspuestamatriz(self):
        m = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        rt = [[[1, 2], [4, 5], [2, 1]], [[2, 3], [5, 6], [5, 5]], [[1, 3], [6, 7], [4, 2]]]
        self.assertEqual(lnc.traspuesta(m), rt)

    def test_conjugadomatriz(self):
        m = [
            [[2, 1], [3, 3], [1, 5]],
            [[2, 2], [3, 3], [5, 2]],
            [[1, 5], [2, 6], [7, 2]]
        ]
        rt = [[(2, -1), (3, -3), (1, -5)], [(2, -2), (3, -3), (5, -2)], [(1, -5), (2, -6), (7, -2)]]
        self.assertEqual(lnc.conjugadomatriz(m), rt)

    def test_adjuntamatriz(self):
        m = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        rt = [[(1, -2), (4, -5), (2, -1)], [(2, -3), (5, -6), (5, -5)], [(1, -3), (6, -7), (4, -2)]]
        self.assertEqual(lnc.adjuntamatriz(m), rt)

    def test_multmatrices(self):
        m1 = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        m2 = [
            [[2, 1], [3, 3], [1, 5]],
            [[2, 2], [3, 3], [5, 2]],
            [[1, 5], [2, 6], [7, 2]]
        ]
        rt = [[(-16, 23), (-22, 36), (-4, 49)], [(-28, 73), (-36, 110), (20, 126)], [(-3, 46), (-1, 67), (36, 68)]]
        self.assertEqual(lnc.multmatrices(m1, m2), rt)

    def test_multmatrizvector(self):
        m = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        v = [[[1, 2]],
             [[1, 2]],
             [[1, 2]]]

        rt = [[(-12, 16)], [(-21, 48)], [(-5, 30)]]
        self.assertEqual(lnc.multmatrices(m, v), rt)

    def test_normavector(self):
        v = [
            [[1, 2], [2, 3], [1, 3]],
            [[4, 5], [5, 6], [6, 7]],
            [[2, 1], [5, 5], [4, 2]]
        ]
        self.assertEqual(lnc.normavector(v), 17.029386365926403)

    def test_unitaria(self):
        m =[
            [(5, 0), (3, 3), (1, 5)],
            [(3, -3), (3, 0), (2, 6)],
            [(1, -5), (2, -6), (3, 0)]
        ]
        rt = [[(69, 0), (56, 28), (-4, 64)], [(56, -28), (67, 0), (30, 48)], [(-4, -64), (30, -48), (75, 0)]]
        self.assertEqual(lnc.matrizunitaria(m), rt)


    def test_hermitiana(self):
        m =[
            [(5, 0), (3, 3), (1, 5)],
            [(3, -3), (3, 0), (2, 6)],
            [(1, -5), (2, -6), (3, 0)]
        ]
        rt = [[(5, 0), (3, 3), (1, 5)], [(3, -3), (3, 0), (2, 6)], [(1, -5), (2, -6), (3, 0)]]
        self.assertEqual(lnc.matrizhermitiana(m), rt)


if __name__ == '__main__':
    unittest.main()
