#!/usr/bin/python3
"""Module that converts an instance to a dictionary for JSON."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
