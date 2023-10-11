#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sub in matrix:
        if len(sub) == 0:
            print()
        for j in range(len(sub)):
            print("{:d}".format(sub[j]), end="\n" if j is len(sub) - 1
                    else " ")
