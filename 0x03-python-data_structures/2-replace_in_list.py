#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx > len(my_list):
        return None
    elif idx < 0:
        return None
    else:
        my_list[idx] = element
        return my_list
