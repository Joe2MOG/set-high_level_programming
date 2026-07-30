#!/usr/bin/python3
"""Divides all elements of a matrix by a number."""


def matrix_divided(matrix, div):
    """Divide each element of matrix by div, rounding to 2 decimals.

    Args:
        matrix: a list of lists of integers or floats.
        div: a number (int or float).

    Returns:
        A new matrix with all values divided by div, rounded to 2 places.

    Raises:
        TypeError: if matrix is not a list of lists of int/float,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: if div equals 0.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
