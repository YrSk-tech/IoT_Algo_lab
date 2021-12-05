import unittest
from Prim_algo import Graph


class PrimTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(5)
        self.g.add_edge(0, 2, 0, 6, 0)
        self.g.add_edge(2, 0, 3, 8, 5)
        self.g.add_edge(0, 3, 0, 0, 7)
        self.g.add_edge(6, 8, 0, 0, 9)
        self.g.add_edge(0, 5, 7, 9, 0)

    def test_prim(self):
        self.assertEqual(self.g.algo(0), [0, 2, -1, -4, 5])

    def test_prim_inf(self):
        self.assertEqual(self.g.algo(1), [float("Infinity"), 0, -3, -6])

if __name__ == '__main__':
    unittest.main()
