#!/usr/bin/python3
"""Test coverage for Square, matching checker-required scenarios."""
import os
import unittest
from models.square import Square


class TestSquareBatch(unittest.TestCase):
    def test_size_and_x(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_size_x_y(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Square("1")
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_x_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Square(1, "2")
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_not_int(self):
        with self.assertRaises(TypeError) as cm:
            Square(1, 2, "3")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_size_negative(self):
        with self.assertRaises(ValueError) as cm:
            Square(-1)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_x_negative(self):
        with self.assertRaises(ValueError) as cm:
            Square(1, -2)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as cm:
            Square(1, 2, -3)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_size_zero(self):
        with self.assertRaises(ValueError) as cm:
            Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 99)
        expected = {"id": 99, "size": 5, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_create_id_only(self):
        s = Square.create(**{"id": 89})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_id_size(self):
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s.x, 2)

    def test_create_full(self):
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_one(self):
        Square.save_to_file([Square(1, 0, 0, 100)])
        with open("Square.json") as f:
            content = f.read()
        self.assertEqual(
            content, '[{"id": 100, "size": 1, "x": 0, "y": 0}]')
        os.remove("Square.json")

    def test_load_from_file_missing(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        Square.save_to_file([Square(3, 1, 2, 5)])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 5)
        self.assertEqual(result[0].size, 3)
        self.assertEqual(result[0].x, 1)
        self.assertEqual(result[0].y, 2)
        os.remove("Square.json")
