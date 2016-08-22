#!/usr/bin/python

'''
You have a sorted list say lst = [1,2,5,6,9,11,12,14]. You are given 2
arguments. The first argument is some number that is present in the list. Lets
say key = 9 and the second argument is count = 3. Now you will have to return a
list with the length equal to count. The returned list is nothing but the
numbers that are closest to the key (In this case 9).

Example. If count is 1 it should return 11. If count is 2 it should return
[11,6]. If there are more than 1 number that matches then you can choose to
return any 1 if the count is reached. lets say count is 2 and you match 6 as
well as 12 for the 2nd number then you can consider either of the number.
'''


def nearest_lst(lst, key, count):
    i = 1
    left = 1
    right = 1
    j = lst.index(key)
    new_lst = []
    while (i <= count):
        if lst[j] - lst[j-left] < lst[j + right] - lst[j]:
            new_lst.append(lst[j-left])
            left += 1
        else:
            new_lst.append(lst[j+right])
            right +=1
        i += 1
    return new_lst


