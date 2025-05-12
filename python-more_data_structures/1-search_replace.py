#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = 0
    new_list = my_list.copy()
    while i < len(my_list):
        if new_list[i] == search:
            new_list[i] = replace
        i += 1
    return new_list
