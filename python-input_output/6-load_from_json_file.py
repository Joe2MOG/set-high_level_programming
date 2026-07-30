#!/usr/bin/python3
"""Module that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Read a JSON file and return the corresponding Python object."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
