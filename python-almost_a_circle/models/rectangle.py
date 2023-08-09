'''
Here we have a subclass of a Base class that will use a private methods as instances and uses an id instance from the Base class
'''
''' import a class Base from models folder'''


from models.base import Base

''' creat a class'''
class Rectangle(Base):
    ''' define the class with private instances'''

    def __init__(self, width, height, x=0, y=0, id=None):
        # initalize the class
        super().__init__(id)
        # private instances of the class.
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    # get the width by getter method
    def width(self):
        return self.__width

    @width.setter
    # set width by setter method
    def width(self, width):
        self.__width = width
    
    @property
    # set height by getter method
    def height(self):
        return self.__height

    @height.setter
    # set height by setter method
    def height(self,height):
        self.__height = height
    
    @property
    # get x by getter method
    def x(self):
        return self.__x

    @x.setter
    # set x by setter method
    def x(self, x):
        self.__x = x
    
    @property
    # get y by getter method
    def y(self):
        return self.__y

    @y.setter
    # set y by setter method
    def y(self, y):
        self.__y = y
    

