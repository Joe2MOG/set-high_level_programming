#!/usr/bin/python3
"""Function to check if object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class (not direct)."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
