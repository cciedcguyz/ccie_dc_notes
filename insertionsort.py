#!/usr/bin/python



def insertion_sort(lst):

    i = 1
    while i <= len(lst) -1:
        tmp = lst[i]
        if i != len(lst) -1:
            if tmp > lst[i+1]:
                lst[i] = lst[i+1]
                lst[i+1] = tmp
        k = i
        while k > 0:
            if lst[k] < lst[k-1]:
                tmp = lst[k]
                lst[k] = lst[k-1]
                lst[k-1] = tmp
            k -= 1
        i += 1

    return lst







