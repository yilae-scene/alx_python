'''
Here we have a subclass of a Base class that will use a private methods as instances and uses an id instance from the Base class
'''
''' import a class Base from models folder'''


''' creat a class'''

from base import Base




#from models.base import Base
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
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        # check the value of x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        # check the value of y
        if type(y) is not int:
            raise TypeError("y must be an integer")
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
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
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
            raise TypeError("height must be an integer")
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
            raise TypeError("x must be an integer")
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
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' define an area that gets its results from height * width
        '''
        return (self.__height * self.__width)

    def display(self):
        '''
        define a method that prints # based on width and height
        '''
        for y in range(self.__y):
            print()
        for i in range(self.height):
            print(' ' * self.__x, end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        '''
        override the str dunder method to print better info
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        ''' right a public method that assigns the argument to each attribute
        '''
        if len(args)> 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x= args[3]
        if len(args)> 4:
            self.y = args[4]
        if len(args)== 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

r1 = Rectangle(10, 10, 10, 10)
print(r1)
r1.update(89)
print(r1)
r1.update(89, 2)
print(r1)
r1.update(89, 2, 3)
print(r1)
r1.update(89, 2, 3, 4)
print(r1)
r1.update(89, 2, 3, 4, 5)
print(r1)

