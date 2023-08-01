#!/usr/bin/python3
'''Module for function is_same_class'''


def is_same_class(obj, a_class):
    '''Verify if obj is an instance of a_class
    Args:
        obj (object): object
        a_class: class
    Returns: Truc if obj is an instance of a_class
    Otherwize False
    '''
    return (True if (type(obj) == a_class) else False)
