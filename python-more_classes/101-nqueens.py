#!/usr/bin/python3
import sys


"""
Module Name: 101-nqueens.py

Description:
    This module include a program that solves the N queens problem.
    The N queens puzzle is the challenge of placing N non-attacking
    queens on an N×N chessboard

Usage:
    ./nqueens N

Author:
    Valentin DUMONT
"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)


def is_safe(row, column, queen_pos):
    """
    Check whether a queen can be safely placed at the given row and column.

    A queen can be placed if there is no other queen in the same column
    or on the same diagonal (positive or negative slope) in any previous row.

    Args:
        row (int): The row index where the queen is to be placed.
        column (int): The column index where the queen is to be placed.
        queen_pos (list): A list of column indices representing the positions
                          of queens already placed in previous rows. The index
                          of the list represents the row, and the value at that
                          index represents the column.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for i in range(row):
        prev_column = queen_pos[i]
        if column == prev_column or abs(column - prev_column) == abs(i - row):
            return False
    return True


def solve(queen_pos, row):
    """
    Recursively solve the N queens problem by placing queens row by row.

    At each recursive step, try placing a queen in each column
    of the current row.
    If the position is safe, place the queen and move to the next row.
    When a full valid configuration is found (row == N), print the solution.

    Args:
        queen_pos (list): A list of column indices representing the positions
                          of queens already placed.
        row (int): The current row index to place the next queen.

    Returns:
        None
    """
    if row == N:
        solution = [[x, y] for x, y in enumerate(queen_pos)]
        print(solution)
        return

    for column in range(N):
        if is_safe(row, column, queen_pos):
            queen_pos.append(column)
            solve(queen_pos, row + 1)
            queen_pos.pop()


solve([], 0)
