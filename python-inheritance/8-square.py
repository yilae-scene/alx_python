'''
class area to calculate that is sub-class of rectangle class
'''
# import a file with number and put it in variable called Rectagle

Rectangle = __import__('7-rectangle').Rectangle


class square(Rectangle):
    '''
    calculate the area from a size that is private
    with some uses of some function of the super class
    '''

    def __init__(self, size):
        self.__size = size

    self.integer_validator(size)

    def area(self):
        return self.__size ** 2
