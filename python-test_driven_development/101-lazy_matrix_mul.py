#!/usr/bin/python3
"""Matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy.matmul.

    Args:
        m_a: first matrix.
        m_b: second matrix.

    Returns:
        The product matrix.
    """
    return np.matmul(m_a, m_b)
