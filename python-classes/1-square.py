#!/usr/bin/python3
"""Define a class Square with a private instance attribute size."""


class Square:
    """A square with a private size."""
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
