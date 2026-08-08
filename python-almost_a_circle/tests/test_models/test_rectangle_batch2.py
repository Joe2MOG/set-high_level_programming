#!/usr/bin/python3
"""Additional Rectangle test coverage."""
import io
import os
import contextlib
import unittest
from models.rectangle import Rectangle


class TestRectangleBatch2(unittest.TestCase):
    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_y(self):
        r = Rectangle(2, 3)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), "##\n##\n##\n")

    def test_display_no_y(self):
        r = Rectangle(2, 3, 2)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), "  ##\n  ##\n  ##\n")

    def test_display_with_x_y(self):
        r = Rectangle(2, 3, 2, 2)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r.display()
        self.assertEqual(buf.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_to_dictionary(self):
        r = Rectangle(5, 7, 1, 2, 99)
        expected = {"id": 99, "width": 5, "height": 7, "x": 1, "y": 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_create_id_only(self):
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)

    def test_create_id_width(self):
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(
            **{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r.x, 3)

    def test_create_full(self):
        r = Rectangle.create(
            **{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_one(self):
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 100)])
        with open("Rectangle.json") as f:
            content = f.read()
        self.assertEqual(
            content,
            '[{"id": 100, "width": 1, "height": 2, "x": 0, "y": 0}]')
        os.remove("Rectangle.json")

    def test_load_from_file_missing(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        Rectangle.save_to_file([Rectangle(3, 4, 1, 2, 5)])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 5)
        self.assertEqual(result[0].width, 3)
        self.assertEqual(result[0].height, 4)
        self.assertEqual(result[0].x, 1)
        self.assertEqual(result[0].y, 2)
        os.remove("Rectangle.json")
