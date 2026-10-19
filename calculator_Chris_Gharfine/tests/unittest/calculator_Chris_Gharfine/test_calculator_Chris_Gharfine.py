"""Run with either PyBuilder or Python's unittest runner."""

from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[3] / "src/main/python"
sys.path.insert(0, str(SOURCE))

from calculator_Chris_Gharfine import (  # noqa: E402
    add, divide, modulus, multiply, power, square_root, subtract,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(-3, 1), -2)

    def test_add_fractional_and_zero(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertEqual(add(7, 0), 7)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_and_zero(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(0, 3), -3)

    def test_subtract_fractional(self):
        self.assertAlmostEqual(subtract(1.5, 0.2), 1.3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_and_zero(self):
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(9, 0), 0)

    def test_multiply_fractional(self):
        self.assertAlmostEqual(multiply(1.5, 0.2), 0.3)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_fractional_and_zero(self):
        self.assertEqual(divide(-5, 2), -2.5)
        self.assertEqual(divide(0, 2), 0)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_negative_fractional_and_zero(self):
        self.assertEqual(modulus(-10, 3), 2)
        self.assertEqual(modulus(10, -3), -2)
        self.assertEqual(modulus(0, 3), 0)
        self.assertAlmostEqual(modulus(5.5, 2), 1.5)

    def test_modulus_by_zero(self):
        with self.assertRaisesRegex(ValueError, "zero divisor"):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_negative_and_zero(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(2, -2), 0.25)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 3), 0)

    def test_power_fractional(self):
        self.assertAlmostEqual(power(9, 0.5), 3)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_zero_and_fractional(self):
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(0.25), 0.5)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

    def test_square_root_negative(self):
        with self.assertRaisesRegex(ValueError, "negative number"):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
