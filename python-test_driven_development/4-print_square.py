#!/usr/bin/python3
"""Prints a square made of '#' characters."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size: the length of the square, must be a non-negative integer.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
