#!/usr/bin/python3
"""
Module Name: 0-add_integer.py

Description:
    "This module include a function to add twe integers"

Functions:
    add_integer(a, b=98): Return the sum of twe numbers.

Usage:
    This module can be imported:
        from 0-add_integer import add_integer
    Or run directly if it contains:
        if __name__ == "__main__":

Author:
    Valentin DUMONT

Date:
    2025-05-13
"""

def add_integer(a, b=98):
    """
    Add two numbers.

    Args:
        a: Integer or float.
        b: Integer or float.

    Returns:
        integer: The result of the addition.

    Raises:
        TypeError: If inputs are not integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
