#!/usr/bin/python3
'''module'''


class Student:
    '''defines a student'''
    def __init__(self, first_name, last_name, age):
        '''init'''
        self.fisrt_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns a dictionary representation'''
        return self.__dict__
