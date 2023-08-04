'''
this is a class that inherits form the base_geomety class
'''
# import a file with number and put it in variable called BaseGeometry
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' the class is subclass of BaseGeometry and uses some function of the super class
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # check for value validation
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
