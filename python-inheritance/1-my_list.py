#!/usr/bin/python3
"""
Module Name: 1-my_list.py

Description:
    This module include a class that prints a sorted list.
"""


class MyList(list):
    """
        This class prints a sorted list.
    """
    def print_sorted(self):
        my_list = sorted(self)
        print(my_list)
