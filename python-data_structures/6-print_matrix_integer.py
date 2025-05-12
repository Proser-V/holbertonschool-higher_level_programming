#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    i = 0

    while i < len(matrix):
        j = 0
        while j < (len(matrix[i]) - 1):
            print('{:d}'.format(matrix[i][j]), end=' ')
            j += 1
        if (len(matrix[i]) - 1) >= 0:
            print('{:d}'.format(matrix[i][j]))
        else:
            print()
        i += 1
    
    return