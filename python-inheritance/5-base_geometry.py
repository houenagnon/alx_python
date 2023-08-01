#!/usr/bin/python3
'''Module that defines a class named BaseGeometry'''


class BaseGeometry:
    '''Class BaseGeometry'''
    def area(self):
        '''Signals that area is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates the value of name
        Args:
            name (str): the value given
            value (int): the value of name
        Exception:
            TypeError if value is not an integer
            ValueError if value is less or equal than 0'''
        
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))