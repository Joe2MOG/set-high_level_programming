#!/usr/bin/python3
"""Tests for Base class."""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_manual(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_one_dict(self):
        d = [{"id": 1, "name": "test"}]
        expected = json.dumps(d)
        self.assertEqual(Base.to_json_string(d), expected)
