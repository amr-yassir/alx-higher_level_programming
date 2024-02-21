#!/usr/bin/python3
'''Module'''
Rectangle = __import__('9-rectangle.py').Rectangle


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
