#!/usr/bin/python3
"""
Module Name: 3-is_kind_of_class.py

Description:
    This module include a function that checks if an object is an instance
    of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    A function that checks if an object is an instance
    of a class that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
