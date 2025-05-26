#!/usr/bin/python3
"""
Module Name: 100-my_int.py

Description:
    This module include a class with inverted operators.
"""


class MyInt(int):
    """
        This class with inverted == and != operators.
    """

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
