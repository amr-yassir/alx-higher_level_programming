#!/usr/bin/python3
'''module'''


class Student:
    '''defines a student'''
    def __init__(self, first_name, last_name, age):
        '''init'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dictionary representation'''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic
