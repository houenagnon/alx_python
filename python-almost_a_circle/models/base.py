"""This module implement the class base witch will be the “base” of all other classes in this project"""

class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor of the class"""

        if (id != None) and (isinstance(id, int)):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
        
# b1 = Base()

# print(b1.id)

# b2 = Base()
# print(b2.id)

# b3 = Base()
# print(b3.id)

# b4 = Base(12)
# print(b4.id)

# b5 = Base()
# print(b5.id)