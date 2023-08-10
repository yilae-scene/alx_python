'''
this is a class that inherits from the class rectangle.
'''

#from rectangle import Rectangle

from models.rectangle import Rectangle

class Square(Rectangle):
    '''  
    a class square that inherits from the rectangle class
    '''
    def __init__(self, size, x = 0, y = 0, id = None):
        ''' class initailizer'''
        super().__init__(size, size, x, y, id) # call the super initalizer
        self.size = self.width
        self.size = self.height

    def __str__(self):
        ''' overload the setter mehtod'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    # getter method for the size 
    def size (self):
        return self.width

    @size.setter
    #  setter method for size
    def size(self, value):
        self.width = value
