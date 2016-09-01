#!/usr/bin/python

# lst1 = [2,5,10]
# lst2 = [1,6,11,100]

#Merge 2 sorted list in BIG O(N) notation

def merge_sorted(lst1,lst2):
    if len(lst1) > len(lst2):
        big_len = len(lst1)
        small_len = len(lst2)
        big_l = lst1
        small_l = lst2
    else:
        big_len = len(lst2)
        small_len = len(lst1)
        big_l = lst2
        small_l = lst1

    new_list = []
    i = 0
    j = 0
    while i <= big_len:
        if j == small_len:
            new_list.extend(big_l[i:])
            break
        elif i == big_len:
            new_list.extend(small_l[j:])
            break

        print "Comparing big[i] vs small[j] big[%d] = %d and  small[%d] = %d " % (i, big_l[i], j, small_l[j])
        if big_l[i] < small_l[j]:
            new_list.append(big_l[i])
            i += 1
        else:
            new_list.append(small_l[j])
            j += 1

    return new_list

