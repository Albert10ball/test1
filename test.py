# encoding =utf-8


import unittest


class test1(unittest.TestCase):

    def test_test1(self):
        self.assertEqual(abs(-20), 20)
        # self.assertEqual(abs(-2), 3)


if __name__ == '__main__':
    unittest.main()



