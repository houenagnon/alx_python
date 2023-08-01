#!/usr/bin/python3
'''Module for function is_kind_of_class'''


def is_kind_of_class(obj, a_class):
    '''Verify if obj is an instance of a_class
    Or an instance of the class that inherits from a_class
    Args:
        obj (object): object
        a_class: class
    Returns: Truc if obj is an instance of a_class
    Otherwize False
    '''
    return (isinstance(obj, a_class))