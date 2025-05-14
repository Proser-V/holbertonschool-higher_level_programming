#!/usr/bin/python3
"""
Module Name: 4-print_square.py

Description:
    This module include a function that prints a square made of "#".

Functions:
    print_square(size): print a square of size length "size".

Usage:
    This module can be imported:
        from 4-print_square import print_square
    Or run directly if it contains:
        if __name__ == "__main__":

Author:
    Valentin DUMONT

Date:
    2025-05-14
"""


def print_square(size):
    """
    Prints a square made of "#".

    Args:
        size: The size length of the square.

    Returns:
        No return value. Prints a square.

    Raises:
        TypeError: If size is not an integer.
        TypeError: If size is a float and less than 0.
        ValueError: If size is an integer less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        print()
        i += 1
