'''
Here we have a subclass of a Base class that will use a private methods as instances and uses an id instance from the Base class
'''
''' import a class Base from models folder'''


''' creat a class'''


# from base import Base




from models.base import Base
class Rectangle(Base):
    ''' define the class with private instances'''

    def __init__(self, width, height, x=0, y=0, id=None):
        # initalize the class
        super().__init__(id)
        # check the value of width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        # check the value of height
        if type(height) is not int:
            raise TypeError("height must be an integer.")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        # check the value of x
        if type(x) is not int:
            raise TypeError("x must be an integer.")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x
        # check the value of y
        if type(y) is not int:
            raise TypeError("y must be an integer.")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    @property
    # get the width by getter method
    def width(self):
        return self.__width

    @width.setter
    # set width by setter method
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer.")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    # set height by getter method
    def height(self):
        return self.__height

    @height.setter
    # set height by setter method
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer.")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    # get x by getter method
    def x(self):
        return self.__x

    @x.setter
    # set x by setter method
    def x(self, value):
        if type(value) is not int:
            raise TypeypeError("x must be an integer.")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    # get y by getter method
    def y(self):
        return self.__y

    @y.setter
    # set y by setter method
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer.")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
