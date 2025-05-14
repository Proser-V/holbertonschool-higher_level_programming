#!/usr/bin/python3
"""
A module to multiply 2 matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy's matmul function.
    """
    if not (np.issubdtype(np.asarray(m_a).dtype, np.number) and np.issubdtype(np.asarray(m_b).dtype, np.number)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    return np.matmul(m_a, m_b)
