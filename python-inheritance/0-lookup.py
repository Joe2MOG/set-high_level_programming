#!/usr/bin/python3
"""Function that returns the list of attributes/methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of obj."""
    return dir(obj)
