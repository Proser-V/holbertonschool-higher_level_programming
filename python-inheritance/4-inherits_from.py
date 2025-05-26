#!/usr/bin/python3
"""
Module Name: 4-inherits_from.py

Description:
    This module include a function that checks if an object is an instance of
    a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    A function that checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
