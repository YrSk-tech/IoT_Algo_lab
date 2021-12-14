import unittest

from algo import Kmp


class KMPTest(unittest.TestCase):
    def testKmp1(self):
        self.assertEqual(Kmp().Search("ASD", "DASTTTAAAADDDOSADHFASDOY"), 0)

    def testKmp2(self):
        self.assertEqual(Kmp().Search("fsdgfhr", "qpwoueazxcpkl"), 0)


if __name__ == '__main__':
    unittest.main()
