#!/usr/bin/python3
"""
Module Name: task_02_verboselist.py

Description:
    This module include a class that extends the Python list class
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
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
