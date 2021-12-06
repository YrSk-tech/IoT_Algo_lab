import unittest
from Prim_algo import Graph


class PrimTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(5)
        self.g.add_edge(0, 1, 17)
        self.g.add_edge(0, 2, 37)
        self.g.add_edge(0, 3, 657)
        self.g.add_edge(0, 4, 345)
        self.g.add_edge(1, 2, 345)
        self.g.add_edge(1, 3, 7467)
        self.g.add_edge(1, 4, 654)
        self.g.add_edge(2, 3, 253)
        self.g.add_edge(2, 4, 213)
        self.g.add_edge(2, 1, 7865)
        self.g.add_edge(3, 1, 123)
        self.g.add_edge(3, 2, 457)
        self.g.add_edge(3, 4, 6457)
        self.g.add_edge(3, 0, 4567)
        self.g.add_edge(4, 0, 4576)
        self.g.add_edge(4, 1, 7456)
        self.g.add_edge(4, 2, 7568)
        self.g.add_edge(4, 3, 353)


    def test_prim(self):
        self.assertEqual(self.g.primMST(0), [True, True, True, True, True])


if __name__ == '__main__':
    unittest.main()
