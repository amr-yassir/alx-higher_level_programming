#!/usr/bin/python3
'''technical interview module'''


def pascal_triangle(n):
    '''returns list of lists of integers representing Pascal’s triangle'''
    if n <= 0:
        return []

    list_n = [[1]]
    while len(list_n) != n:
        list_t = list_n[-1]
        temp = [1]
        for i in range(len(list_t) - 1):
            temp.append(list_t[i] + list_t[i + 1])
        temp.append(1)
        list_n.append(temp)
    return list_n
