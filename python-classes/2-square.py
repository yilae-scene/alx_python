''' this is the first and most basic class
    creation that uses a private variable.
'''
class Square:
    ''' defining the class of square and initializing it with a variable size '''

    def __init__(self, size = 0):
        ''' the first init function that has a single
            parameter that is also privare.
        '''

        if not isinstance(size, int):
            # check the type of size
            raise TypeError ('size must be an integer')
        elif size < 0:
            # check the value of size
            raise ValueError('size must be >= 0')
        else:
            # if  all is correct print
            self.__size = size

    def area(self):
        # find the area of the square by multiplying itself
        return self.__size ** 2



