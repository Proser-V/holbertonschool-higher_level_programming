#!/usr/bin/python3
"""
A module to multiply 2 matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy's matmul function.
    """
    return np.matmul(m_a, m_b)
