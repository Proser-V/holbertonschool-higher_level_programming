#!/usr/bin/python3
"""
Module Name: 2-is_same_class.py

Description:
    This module include a function that checks if an object is exactly
    an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    A function that checks if an object is exactly an instance of the
    specified class.
    """
    return type(obj) is a_class
