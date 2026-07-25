#!/usr/bin/python3
"""MyInt class that inherits from int with inverted == and !=."""


class MyInt(int):
    """Rebel integer with swapped equality operators."""

    def __eq__(self, other):
        """Return False when == is used."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True when != is used."""
        return super().__eq__(other)
