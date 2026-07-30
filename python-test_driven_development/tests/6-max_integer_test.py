#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-3]), -3)

    def test_positive_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_ints(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([10, 10, 1]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_list_with_one_negative(self):
        self.assertEqual(max_integer([-5]), -5)

if __name__ == "__main__":
    unittest.main()
