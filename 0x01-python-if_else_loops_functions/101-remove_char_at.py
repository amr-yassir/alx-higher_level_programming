#!/usr/bin/python3

def remove_char_at(str, n):
    str_cpy = ""
    for i, c in enumerate(str):
        if i != n:
            str_cpy += c
    return str_cpy
