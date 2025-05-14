#!/usr/bin/python3
"""
Module Name: 2-matrix_divided.py

Description:
    This module include a function that divides all elements of a matrix.

Functions:
    matrix_divided(matrix, div): Returns a new matrix with divided numbers.

Usage:
    This module can be imported:
        from 2-matrix_divided import matrix_divided
    Or run directly if it contains:
        if __name__ == "__main__":

Author:
    Valentin DUMONT

Date:
    2025-05-13
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: List of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        List: A new matrix with divided numbers (2 decimals).

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If every row of matrix are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError : If div = 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []

    row_length = len(matrix[0])
    for row in matrix:
        new_row = []
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = round(elem / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
