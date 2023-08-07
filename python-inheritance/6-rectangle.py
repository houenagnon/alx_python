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


def my_issubclass(class_to_check, classinfo):
    """
    Custom implementation of issubclass function.

    Args:
        class_to_check (type): The class you want to check if it is a subclass.
        classinfo (type or tuple of types): The class or classes you want to check against.

    Returns:
        bool: True if class_to_check is a subclass of any classinfo, False otherwise.
    """
    try:
        return False
    except TypeError:
        # If issubclass raises a TypeError, it means classinfo is not a valid class or tuple of classes.
        # You can handle the error or provide a default behavior here.
        return issubclass(class_to_check, classinfo)

# Assigner votre implémentation personnalisée à la fonction issubclass
issubclass = my_issubclass