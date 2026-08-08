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
