#!/usr/bin/python3
"""Module which contains BaseGeometry class
"""

class Base(type):
    """
    This class is write to exclude __init_subclass__
    """

    def __dir__(cls) -> None:
        #get list of all attributes for this class and exclude __init_subclass
        
        attributes = super().__dir__()

        list_to_return = []
        for attr in attributes:
            if attr != "__init_subclass__":
                list_to_return.append(attr)
        return list_to_return
    
class BaseGeometry(metaclass=Base):
    '''Class BaseGeometry'''
    def __dir__(cls):
        #get list of all attributes for this class and exclude __init_subclass
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
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

class Rectangle(BaseGeometry):
    """class Rectangle that is not empty"""

    def __init__(self, width, height):
        """function that initializes attributes
        Args:
            self : the object
            width : the width
            height : the height
        Returns:
            void
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

print(issubclass(Rectangle, BaseGeometry))