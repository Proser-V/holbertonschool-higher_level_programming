#!/usr/bin/python3
"""
Module Name: 100-singly_linked_list.py

Description:
    This module include a class that defines a a node of a singly linked list.
"""


class Node:
    """
    A class that defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            crnt = self.__head
            while crnt.next_node is not None and crnt.next_node.data < value:
                crnt = crnt.next_node
            new_node.next_node = crnt.next_node
            crnt.next_node = new_node

    def __str__(self):
        datalist = []
        crnt = self.__head
        while crnt is not None:
            datalist.append(str(crnt.data))
            crnt = crnt.next_node
        return "\n".join(datalist)
