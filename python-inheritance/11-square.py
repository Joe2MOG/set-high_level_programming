#!/usr/bin/python3
"""Square class with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that prints [Square] <size>/<size>."""

    def __init__(self, size):
        """Initialize a new Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
