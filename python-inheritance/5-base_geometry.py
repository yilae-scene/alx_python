'''
    a class that raises an error if not implemented
'''


class BaseGeometry:
    ''' the class raises a an exception'''

    def __dir__(self):
        ''' remover the "__init_subclas__" in the subclass'''
        attributes = super().__dir__()
        return [x for x in attributes if x != '__init_subclass__']

    def area(self):
        # raise an error
        raise Exception('area() is not implemented')

    def integer_validator(self,name,value):
        # checks for value if if fullfills certain checks
        self.name = name
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0 :
            raise ValueError ('{} must be greater than 0'.format(self.name))

