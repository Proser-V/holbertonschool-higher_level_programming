#!/usr/bin/python3

"""
Description: A function that returns a list of lists of integer representing
that Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integer representing
    that Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
