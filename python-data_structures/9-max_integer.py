#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    i = 0
    max_int = 0
    while i < len(my_list):
        if max_int < my_list[i]:
            max_int = my_list[i]
        else:
            pass
        i += 1
    return max_int
