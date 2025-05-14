#!/usr/bin/python3
"""
A module to multiply 2 matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplie deux matrices en utilisant la fonction matmul de numpy.
    """
    return np.matmul(m_a, m_b)
