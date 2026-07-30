#!/usr/bin/python3
"""Matrix multiplication using NumPy with input validation."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy.matmul.

    Args:
        m_a: first matrix.
        m_b: second matrix.

    Returns:
        The product matrix.
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check multiplication compatibility
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
