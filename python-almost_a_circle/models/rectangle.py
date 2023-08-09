'''
Here we have a subclass of a Base class that will use a private methods as instances and uses an id instance from the Base class
'''
''' import a class Base from models folder'''


''' creat a class'''

#from base import Base




from models.base import Base
class Rectangle(Base):
    ''' define the class with private instances'''

    def __init__(self, width, height, x=0, y=0, id=None):
        # initalize the class
        super().__init__(id)
        # private instances of the class.
        # check for width
        if not isinstance(width, int):
            raise TypeError("width must be an integer.")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        # check for height
        if not isinstance(height, int):
            raise TypeError("height must be an integer.")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        # check for x
        if not isinstance(x, int):
            raise TypeError("x must be an integer.")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        # check for y
        if not isinstance(y, int):
            raise TypeError("y must be an integer.")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    # get the width by getter method
    def width(self):
        return self.__width

    @width.setter
    # set width by setter method
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer.")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    # set height by getter method
    def height(self):
        return self.__height

    @height.setter
    # set height by setter method
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer.")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    # get x by getter method
    def x(self):
        return self.__x

    @x.setter
    # set x by setter method
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer.")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    # get y by getter method
    def y(self):
        return self.__y

    @y.setter
    # set y by setter method
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer.")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
