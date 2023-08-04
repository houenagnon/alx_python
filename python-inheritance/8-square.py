#!/usr/bin/python3
"""Module which contains Square class
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''
    def __init__(self, size):
        '''initialization
        Args:
            size (int): size of a side
        '''
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        '''How print a rectangle'''
        return ("[Square] {}/{}".format(self.__size, self.__size))