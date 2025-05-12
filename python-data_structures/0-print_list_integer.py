#!/usr/bin/python3

def print_list_integer(my_list=[]):
    i = 0
    while i < len(my_list):
        str = '{}'.format(my_list[i])
        print(str)
        i += 1
