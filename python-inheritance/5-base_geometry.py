''' 
 meta class that will provide the dir method to BaseGeometry class
'''


class TopMeta(type):
    ''' 
        remove the init__subclass so that BaseGeomety will be without it
    '''

    def __dir__(self):
        # use an overloading to remove the 'initsubclass'
        attributes = super().__dir__()
        return [x for x in attributes if x != '__init_subclass__']


class BaseGeometry (metaclass=TopMeta):

    ''' the class raises a an exception'''

    def __dir__(self):
        ''' remover the "__init_subclas__" in the subclass'''
        attributes = super().__dir__()
        return [x for x in attributes if x != '__init_subclass__']

    def area(self):
        # raise an error
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        # checks for value if if fullfills certain checks
        self.name = name
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
