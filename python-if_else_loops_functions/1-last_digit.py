#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
digit = number % 10

if digit < 6 and digit != 0:
    print('{} {} is {} and is less than 6 and not 0'.format(string, number, digit))
if digit == 0:
    print('{} {} is {} and is 0'.format(string, number, digit))
if digit > 5:
    print('{} {} is {} and is greater than 5'.format(string, number, digit))
