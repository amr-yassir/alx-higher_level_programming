#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("0 arguments.")
    elif argv_len == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argv_len - 1))
        i = 1
        while i < argv_len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
