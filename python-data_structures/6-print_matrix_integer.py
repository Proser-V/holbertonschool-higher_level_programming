#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    i = 0
    if matrix == None:
        return
    while i < len(matrix):
        print('{}'.format(matrix[i]))
        i += 1
    
    return