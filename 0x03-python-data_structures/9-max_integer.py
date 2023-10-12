#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = my_list.copy()
    new_list.sort()
    m = new_list.pop()
    return m if len(my_list) > 0 else None
    
