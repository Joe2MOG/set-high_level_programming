#!/usr/bin/python3
"""BaseGeometry with area() that raises Exception."""


class BaseGeometry:
    """Base class with unimplemented area method."""

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
