#!/usr/bin/python3
"""Multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: first matrix, list of lists of int/float.
        m_b: second matrix, list of lists of int/float.

    Returns:
        The product matrix.

    Raises:
        TypeError: if inputs are not lists of lists, contain non-numbers,
                   or rows are not all the same size.
        ValueError: if matrices are empty or cannot be multiplied.
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

    # Validate m_b similarly
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

    # Can they be multiplied?
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiplication
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            dot = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            new_row.append(dot)
        result.append(new_row)
    return result
