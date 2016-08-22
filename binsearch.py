#!/usr/bin/python




def binsearch(lst,item):
    start = 0
    end = len(lst)

    while start <= end:
        mid = (start + end) / 2
        print 'item in lst[mid] is %d' % lst[mid]
        if item == lst[mid]:
            print 'Your Number %d is present in the list in this index %d' % (item,mid)
            break
        elif item < lst[mid]:
            print 'Number is present in left side'
            end = mid - 1
        elif item > lst[mid]:
            print 'Number is present in right side'
            start = mid + 1

