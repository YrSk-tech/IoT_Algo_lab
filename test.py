import unittest

from electr import Algo


class ElectrTest(unittest.TestCase):
    def SetUp(self):
        self.a = Algo()
        self.a.input_data(23)
        self.a.input_data(23)
        self.a.input_data(23)

    def test_electr(self):
        self.assertEqual(self.a.electr(100), 300)

if __name__ == '__main__':
    unittest.main()