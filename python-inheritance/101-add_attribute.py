#!/usr/bin/python3
"""
Module Name: 101-add_attribute.py

Description:
    This module include a function that adds a new attribute to an
    object if it is possible.
"""


def add_attribute(object, name, value):
    """
        A function that adds a new attribute to an object if it is possible.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)
