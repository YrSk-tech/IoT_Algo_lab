import unittest

from algo import Kmp


class KMPTest(unittest.TestCase):
    def testKmp2(self):
        self.assertEqual(Kmp().Search("fsdgfhr", "qpwoueazxcpkl"), None)


if __name__ == '__main__':
    unittest.main()
