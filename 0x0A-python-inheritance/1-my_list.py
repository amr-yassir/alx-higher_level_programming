#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """printing sorted list"""
        print(sorted(self))
