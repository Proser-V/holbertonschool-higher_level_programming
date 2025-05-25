#!/usr/bin/python3
"""
Module Name: 0-lookup.py

Description:
    This module include a function that returns the list of
    available attributes and methods of an object.
"""

def lookup(obj):
    """
    A function that returns the list of available attributes
    and methods of an object.
    """
    return dir(obj)
