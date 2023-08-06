#!/usr/bin/python3

'''Module that defines a class named BaseGeometry'''

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

    def __dir__(cls) -> None:
        #get list of all attributes for this class and exclude __init_subclass
        
        attributes = super().__dir__()

        list_to_return = []
        for attr in attributes:
            if attr != "__init_subclass__":
                list_to_return.append(attr)
        return list_to_return
   
    pass


bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))