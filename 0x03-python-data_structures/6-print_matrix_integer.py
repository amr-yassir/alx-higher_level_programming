#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sub in matrix:
        if len(sub) == 0:
            print()
        for j in range(len(sub)):
            print("{:d}".format(sub[j]))
            if j == len(sub) - 1:
                print()
            else:
                print(" ")
