#!/usr/bin/python3
"""Define a MagicClass that matches given bytecode."""
import math


class MagicClass:
    """A circle class with radius."""
    def __init__(self, radius=0):
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self._MagicClass__radius
