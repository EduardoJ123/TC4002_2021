import math
import unittest


class MathCeilTest(unittest.TestCase):
    # RIGHT testing
    def test_pi(self):
        self.assertAlmostEqual(math.ceil(3.1416), 4)

    def test_e(self):
        self.assertAlmostEqual(math.ceil(2.71), 3)

    def test_zero(self):
        self.assertAlmostEqual(math.ceil(0), 0)

    def test_integer(self):
        self.assertAlmostEqual(math.ceil(100), 100)

    # Boundary testing
    def test_near_zero(self):
        self.assertAlmostEqual(math.ceil(0.00001), 1)

    def test_near_one(self):
        self.assertAlmostEqual(math.ceil(0.99999), 1)

    def test_big_float(self):
        self.assertAlmostEqual(math.ceil(999999.9999999999), 1000000)

    # Inverse testing
    def test_negative_float(self):
        self.assertAlmostEqual(math.ceil(-1.1), -1)

    def test_negative_integer(self):
        self.assertAlmostEqual(math.ceil(-100), -100)

    def test_negative_near_zero(self):
        self.assertAlmostEqual(math.ceil(-0.00001), 0)

    # Error testing
    def test_err_string(self):
        with self.assertRaises(TypeError):
            math.ceil("string")


if __name__ == '__main__':
    unittest.main()
