#!/usr/bin/python3
from abc import ABC, abstractmethod


"""
Module Name: task_00_abc.py

Description:
    This module include an abstract class and subclasses
"""


class Animal(ABC):
    """
        An abstract class with abstract method for sub classes
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
        A subclass for a typical object
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
        A subclass for a typical object
    """
    def sound(self):
        return "Meow"
