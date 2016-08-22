#!/usr/bin/python




def binsearch(lst,item):

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = len(lst) / 2
        if item == lst[mid]:
            print 'Your Number %d is present in the list in this index' % mid
        elif item < lst[mid]

