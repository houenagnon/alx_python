"""This module implement square class"""

from rectangle import Rectangle

class Square(Rectangle):
    """This class inherit from Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))