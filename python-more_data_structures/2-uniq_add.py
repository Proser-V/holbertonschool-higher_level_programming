#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    set_list = set(my_list)

    for number in set_list:
        result += number
    return result
