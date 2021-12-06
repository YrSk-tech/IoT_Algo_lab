import unittest
from Prim_algo import Graph


class PrimTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(5)
        self.g.add_edge(0, 2, 0, 6, 0)
        self.g.add_edge(2, 0, 3, 8, 5)
        self.g.add_edge(0, 3, 0, 0, 7)
        self.g.add_edge(0, 0, 0, 0, 0)
        self.g.add_edge(0, 0, 0, 0, 0)

    def test_prim(self):
        self.assertEqual(self.g.primMST(0), [True, True, True, True, True])


if __name__ == '__main__':
    unittest.main()
