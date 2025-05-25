#!/usr/bin/python3
"""
Module Name: 1-my_list.py

Description:
    This module include a class "MyList" that inherits from "list".
"""


class MyList(list):
    def print_sorted(self):
        my_list = sorted(self)
        print(my_list)
