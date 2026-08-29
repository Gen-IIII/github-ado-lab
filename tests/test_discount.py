import unittest

from src.discount import total_after_discount


class DiscountTest(unittest.TestCase):
    def test_applies_discount(self) -> None:
        self.assertEqual(total_after_discount(1000, 0.2), 800.0)

    def test_rejects_invalid_rate(self) -> None:
        with self.assertRaises(ValueError):
            total_after_discount(1000, 1.1)

    def test_rejects_negative_subtotal(self) -> None:
        with self.assertRaises(ValueError):
            total_after_discount(-100, 0.2)


if __name__ == "__main__":
    unittest.main()
