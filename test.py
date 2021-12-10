import unittest

from electr import Electr


class ElectrTest(unittest.TestCase):

    def test_electr1(self):
        self.assertEqual(Electr(2, [3, 1, 3]).get_cable_length(), 5.66)

    def test_electr2(self):
        self.assertEqual(Electr(100, [1, 1, 1, 1]).get_cable_length(), 300)


if __name__ == '__main__':
    unittest.main()
