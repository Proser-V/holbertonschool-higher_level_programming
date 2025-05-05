#!/usr/bin/python3

def print_last_digit(number):
    dgt = number % 10
    if number < 0:
        dgt = (dgt - 10) * -1

    print('{}'.format(dgt), end="")
    return dgt
