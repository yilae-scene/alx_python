''' this is the first and most basic class
    creation that uses a private variable.
'''


class Square:
    ''' defining the class of square and initializing it with a variable size '''

    def __init__(self, size):
        ''' the first init function that has a single
            parameter that is also privare.
        '''
        if not isinstance(size, int):
            raise TypeError ('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self__size = size


my_square_4 = Square(-89)
print(type(my_square_4))
print(my_square_4.__dict__)
