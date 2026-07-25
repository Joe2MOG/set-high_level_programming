#!/usr/bin/python3
"""Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square with size validation."""

    def __init__(self, size):
        """Initialize a new Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
