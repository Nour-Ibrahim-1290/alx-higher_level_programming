#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weighted_sum = sum([score[0] * score[1] for score in my_list])
    weights = sum([score[1] for score in my_list])
    return weighted_sum / weights
