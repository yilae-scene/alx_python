'''
this is a rectangle class that inherits from its parent class Base class.
'''
Base = __import__('base').Base

''' 
lets import the Base class from base class py.
'''


class Rectangle(Base):
    '''
    here we have an private instance variables that have there own setters and getters.
    '''
    # private attributes:
    # __width
    # __height
    # __x
    # __y

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    # get the width return through width getter
    def width(self):
        return self.__width

    @width.setter
    # get the width set through width setter
    def width(self, width):
        self.__width = width

    @property
    # get the height returned through height getter
    def height(self):
        return self.__height

    @height.setter
    # set the height set through height setter
    def height(self, height):
        self.__height = height

    @property
    # get the x  through x getter
    def x(self):
        return self.__x

    @x.setter
    # set the x through x setter
    def set_width(self, x):
        self.__x = x

    @property
    # get the y through y getter
    def y(self):
        return self.__y

    @y.setter
    # set the y through y setter
    def y(self, Y):
        self.__y = y
