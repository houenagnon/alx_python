"""This module implement square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """This class inherit from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the init method of the class"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """This method is to print the information about the class"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    def get_size():
        """This is the getter of size"""
        return super().width
    def set_size(size):
        """This is the setter of size"""
        super().width(size)
        super().height(size)