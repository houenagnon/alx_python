#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle'''
    def __init__(self, width, height):
        '''Initialization
        Args:
            width (int): width of rectangle
            height (int): height og rectangle
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height