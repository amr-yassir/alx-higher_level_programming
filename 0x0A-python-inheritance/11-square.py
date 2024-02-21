#!/usr/bin/python3
'''Module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''inherits from Rectangle'''
    def __init__(self, size):
        '''init'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''returns area'''
        return self.__size ** 2

    def __str__(self):
        '''string representation'''
        return "[Square] " + str(self.__width) + "/" + str(self.__height)
