#!/usr/bin/python3
"""
Module Name: task_05_dragon.py

Description:
    Studying the mixin concept.
"""


class SwimMixin:
    """
        A class Fish.
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
        A class Bird.
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
        A subclass with multiple inheritence.
    """

    def roar(self):
        print("The dragon roars!")
