#!/usr/bin/python


'''
Write a function which takes 2 arguments as inputs. The first argument is an
integer and the second argument is a list of numbers. The function should return
a list of tuples where each tuple is the pair of numbers which will sum up to
the integer given.

Example: a = 10 and b = [1,9,2,3,7,6,5] a and b are the input and the result
should be [(1,9), (3,7)]
'''



def remove_dups_from_list(lst):

    i = 0
    while i <= len(lst):
        #import pdb; pdb.set_trace()
        tmp = list(lst[i])
        tmp.reverse()
        tmp = tuple(tmp)
        lst[i] = tmp
        lst = list(set(lst))
        i += 1

    return lst

    

    


