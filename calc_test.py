import unittest


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, 2 + 2)

    def test_sub(self):
        self.assertEqual(2, 4 - 2)


if __name__ == '__main__':
    unittest.main()
