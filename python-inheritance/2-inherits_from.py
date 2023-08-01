#!/usr/bin/python3
'''Module for the function inhertis_from'''


def inherits_from(obj, a_class):
    '''Verify if obj is an instance of a class that inherits from a_class
    Args:
        obj (object): object
        a_class: class
    Returns: Truc if obj is an instance of a_class
    Otherwize Fals
    '''
    return (True if issubclass(type(obj), a_class) and
            (type(obj) != a_class) else False)