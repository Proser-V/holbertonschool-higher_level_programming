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
    for i in range(row):
        prev_column = queen_pos[i]
        if column == prev_column or abs(column - prev_column) == abs(i - row):
            return False
    return True

def solve(queen_pos, row):
    if row == N:
        solution =[[x, y] for x, y in enumerate(queen_pos)]
        print(solution)
        return

    for column in range(N):
        if is_safe(row, column, queen_pos):
            queen_pos.append(column)
            solve(queen_pos, row + 1)
            queen_pos.pop()

solve([], 0)