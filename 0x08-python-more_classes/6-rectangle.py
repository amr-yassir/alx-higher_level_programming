#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """ Represents a rectangle """
    def __init__(self, width=0, height=0, number_of_instances=0):
        """Initialization"""
        self.width = width
        self.height = height
        self.number_of_instances = number_of_instances

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """represents the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        rec += "\n".join('#' * self.__width for i in range(self.__height))
        return rec

    def __repr__(self):
        """Returns a string representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a farewell message"""
        self.number_of_instances --
        print("Bye rectangle...")


