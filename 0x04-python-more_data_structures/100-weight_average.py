#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_w = sum(map(lambda pair: pair[0] * pair[1], my_list))
    return sum_w / sum(map(lambda pair: pair[1], my_list))
