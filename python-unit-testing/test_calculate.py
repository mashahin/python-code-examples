import unittest
import calculate


class Testcalculate(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate.add(10, 5), 15)
        self.assertEqual(calculate.add(-1, 1), 0)
        self.assertEqual(calculate.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculate.subtract(10, 5), 5)
        self.assertEqual(calculate.subtract(-1, 1), -2)
        self.assertEqual(calculate.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculate.multiply(10, 5), 50)
        self.assertEqual(calculate.multiply(-1, 1), -1)
        self.assertEqual(calculate.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calculate.divide(10, 5), 2)
        self.assertEqual(calculate.divide(-1, 1), -1)
        self.assertEqual(calculate.divide(-1, -1), 1)
        self.assertEqual(calculate.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calculate.divide(10, 0)


if __name__ == '__main__':
    unittest.main()