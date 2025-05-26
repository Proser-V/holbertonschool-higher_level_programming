#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


"""
Module Name: task_01_duck_typing.py

Description:
    This module include an abstract class and subclasses.
    Another function simulate duck-typing.
"""


class VerboseList(list):
    """
        A class that extends the Pyhton list class
    """

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        count = 0
        for i in items:
            count += 1
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list".format(item))
