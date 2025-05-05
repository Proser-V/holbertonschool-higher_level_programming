#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
dgt = number % 10
if number < 0:
    dgt = dgt - 10
if dgt < 6 and dgt != 0:
    print('{} {} is {} and is less than 6 and not 0'.format(str, number, dgt))
if dgt == 0:
    print('{} {} is {} and is 0'.format(str, number, dgt))
if dgt > 5:
    print('{} {} is {} and is greater than 5'.format(str, number, dgt))
