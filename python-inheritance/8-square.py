''' class area to calculate that is sub-class of rectangle class
this is a class that inherits form the base_geomety class
'''

# import a file with number and put it in variable called Rectagle
Rectangle = __import__('7-rectangle').Rectangle

'''
class area to calculate that is sub-class of rectangle class
'''


class Square(Rectangle):
    '''
    calculate the area from a size that is private
    with some uses of some function of the super class
    '''

    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

s = Square(13)

print(s)
print(s.area())
'''
s = Square(13)

print(s)
print(s.area())
'''
