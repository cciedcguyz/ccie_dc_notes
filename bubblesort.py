#!/usr/bin/python



def bubble_sort(lst):

    for x in lst:
        j = 0
        while (j < len(lst) - 1):
            if lst[j] > lst[j+1]:
                greater = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = greater
            j += 1
    return lst


