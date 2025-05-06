#!/usr/bin/python3

def remove_char_at(str, n):
    cpy = '{}{}'.format(str[:n], str[(n + 1):], end="")
    return cpy