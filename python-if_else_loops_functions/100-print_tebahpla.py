#!/usr/bin/python3

j = 89
i = 122
for i in range(122, 97, -2):
    print('{}{}'.format(chr(i), chr(j)), end="")
    j = j - 2
