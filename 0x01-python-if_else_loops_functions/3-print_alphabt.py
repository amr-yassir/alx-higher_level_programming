#!/usr/bin/python3
"""print the alphabet in lowercase, except q and e"""

for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{}".format(chr(i)), end="")
