#!/usr/bin/python3
""" Class that defines a rectangle """


class Rectangle:
    """ defines a rectangle by width & height """

    def __init__(self, width = 0, height = 0):
        """Initialization"""
        self._width = width     # private attribute
        self._height = height   # private attribute

    @property
    def width(self):
        """retrieve the width"""
        return self._width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """retrieve the height"""
        return self._height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
