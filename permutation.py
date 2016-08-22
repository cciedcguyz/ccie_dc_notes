#!/usr/bin/python




def permu(lst):


    if len(lst) == 1:
        return [lst]

    n_lst = []
    for x in range(len(lst)):
        f_ele = [lst[x]]
        r_lst = lst[:x] + lst[x+1:]

        for j in permu(r_lst):
            n_lst.append(f_ele + j)
    return n_lst


