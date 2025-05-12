#!/usr/bin/python3

def no_c(my_string):
    i = 0
    new_list = []
    while i < len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            new_list.append(my_string[i])
        i += 1
    new_string = ''.join(new_list)
    return new_string
