#!/usr/bin/python3
"""
Module Name: 2-square.py

Description:
    This module include an empty class that defines a square.
"""


class Square:
    """
    An empty class that defines a square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
