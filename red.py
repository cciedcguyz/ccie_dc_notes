#!/usr/bin/python


def sum_of_n_numbers(lst):
    sum = 0
    for x in lst:
        sum += x
    return sum


def sum_of_nums(lst):

    return reduce(lambda x,y: x+y, lst)
