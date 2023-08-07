"""This module implement the class Rectangle inherits from Base"""
from models.base import Base
class Rectangle(Base):
    "This class inherits from class Base and modelize a rectangle"

    def __init__(self,width, height, x=0, y=0, id=None):
        """This is the constructor of the class rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    #Definition of getter's and setter's of each variable

    ## About the width variable
    def get_width(self):
        """Get the value of __width"""
        return self.__width
    def set_width(self, width):
        """Set the value of __width"""
        self.__width = width
    
    width = property(get_width, set_width)
    ## About the height variable
    def get_height(self):
        """Get the value of __height"""
        return self.__height
    def set_height(self, height):
        """Set the value of __height"""
        self.__height = height

    height = property(get_height, set_height)

    ## About the x variable
    def get_x(self):
        """Get the value of __x"""
        return self.__x
    def set_x(self, x):
        """Set the value of __x"""
        self.__x = x
    
    x = property(get_x, set_x)

    ## About the y variable
    def get_y(self):
        """Get the value of __y"""
        return self.__y
    def set_y(self, y):
        """Set the value of __y"""
        self.__y = y

    y = property(get_y, set_y)
    
# r1 = Rectangle(10, 2)
# print(r1.id)

# r2 = Rectangle(2, 10)
# print(r2.id)

# r3 = Rectangle(10, 2, 0, 0, 12)
# print(r3.id)

# print(r3.get_height())
