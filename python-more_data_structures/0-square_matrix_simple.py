#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    while i < len(matrix):
        row = []
        j = 0
        while j < len(matrix[i]):
            row.append(matrix[i][j] ** 2)
            j += 1
        new_matrix.append(row)
        i += 1
    return new_matrix
