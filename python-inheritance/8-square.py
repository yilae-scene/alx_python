'''
area to calculate that is sub-class of rectangle
''' 
Rectangle =__import__('7-rectangle').Rectangle

class square(Rectangle):
    '''calculate the area from a size that is private
    '''
    def __init__(self,size):
        self.__size = size

    self.integer_validator(size)

    def area(self):
        return self.__size ** 2
