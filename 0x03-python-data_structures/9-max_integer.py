#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = my_list.copy()
    new_list.sort()
    return (new_list[-1] if len(my_list) > 0 else None)
