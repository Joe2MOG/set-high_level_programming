#!/usr/bin/python3
"""Adds two integers together.

This module provides a single function to add two numbers
after ensuring they are integers. Floats are cast to integers.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as an integer.

    a and b must be integers or floats; otherwise, raise TypeError.
    Float arguments are cast to int before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
