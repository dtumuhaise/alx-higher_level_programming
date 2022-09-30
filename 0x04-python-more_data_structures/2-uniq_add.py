#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    for i in my_list:
        total = sum(list(set(my_list)))
    return total
