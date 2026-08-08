#!/usr/bin/python3
"""Tests for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def test_creation(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_area(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_non_int_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_update_args(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(10)
        self.assertEqual(r.id, 10)
        r.update(10, 5)
        self.assertEqual(r.width, 5)

    def test_height_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_x_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, 2, "3")
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_height_negative(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, -2)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_width_zero(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_zero(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 0)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_negative(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 2, -3)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(cm.exception), "y must be >= 0")
