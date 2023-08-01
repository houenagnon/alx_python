#!/usr/bin/python3

'''Module that defines a class named BaseGeometry'''

class BaseGeometry:
    '''Class BaseGeometry'''
    
    def area(self):
        '''Signals that area is not implemented'''
        raise Exception("area() is not implemented")