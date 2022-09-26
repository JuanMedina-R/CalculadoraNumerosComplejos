import unittest
import Capitulo3 as cap3
import math


class TestCplxOperations(unittest.TestCase):
    def test_booleano(self):
        m = [
            [[0, 0], [1, 0], [0, 0]],
            [[1, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [1, 0]]
        ]
        v = [
            [[2, 0]],
            [[4, 0]],
            [[4, 0]]
        ]
        rt = [[(4, 0)],
              [(2, 0)],
              [(4, 0)]]
        self.assertEqual(cap3.expcanicas(m, v, 3), rt)

    def test_probabilistico(self):
        m = [
            [[0, 0], [1 / 6, 0], [5 / 6, 0]],
            [[1 / 3, 0], [1 / 2, 0], [1 / 6, 0]],
            [[2 / 3, 0], [1 / 3, 0], [0, 0]]
        ]
        v = [
            [[1 / 6, 0]],
            [[1 / 6, 0]],
            [[2 / 3, 0]]
        ]
        rt = [[(21 / 36, 0.0)],
              [(9 / 36, 0.0)],
              [(6 / 36, 0.0)]]
        self.assertEqual(cap3.expprobabilistico(m, v, 1), rt)

    def test_cuantico(self):
        m = [
            [[1 / math.sqrt(2), 0], [1 / math.sqrt(2), 0], [0, 0]],
            [[0, -1 / math.sqrt(2)], [0, 1 / math.sqrt(2)], [0, 0]],
            [[0, 0], [0, 0], [0, 1]]
        ]
        v = [
            [[1 / math.sqrt(3), 0]],
            [[0, 2 / math.sqrt(15)]],
            [[math.sqrt(2 / 5), 0]]
        ]
        rt = [[(0.408248290463863, 0.36514837167011066)],
              [(-0.36514837167011066, -0.408248290463863)],
              [(0.0, 0.6324555320336759)]]
        self.assertEqual(cap3.expcuantico(m, v, 1), rt)


if __name__ == '__main__':
    unittest.main()
