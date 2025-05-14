#!/usr/bin/python3

def weight_average(my_list=[]):
    result = 0
    count = 0
    if len(my_list) == 0:
        return 0
    else:
        for i in range(len(my_list)):
            element = my_list[i]
            weight = element[1]
            score = element[0]
            result += weight * score
            count += weight
    return result / count
