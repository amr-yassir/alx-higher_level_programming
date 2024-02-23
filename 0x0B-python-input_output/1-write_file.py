#!/usr/bin/python3
'''Module'''


def write_file(filename="", text=""):
    '''writes a string to a text file (UTF8)
    returns the number of characters'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        for char in text:
            char += 1
        return char
