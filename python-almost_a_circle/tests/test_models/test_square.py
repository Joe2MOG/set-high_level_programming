#!/usr/bin/python3
"""Tests for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def test_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(3)
        s.size = 7
        self.assertEqual(s.width, 7)
        self.assertEqual(s.height, 7)

    def test_str(self):
        s = Square(4, 2, 1, 10)
        self.assertIn("[Square] (10) 2/1 - 4", str(s))

    def test_update_kwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(size=9, x=3)
        self.assertEqual(s.size, 9)
        self.assertEqual(s.x, 3)
