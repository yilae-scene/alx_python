'''
    a class that raises an error if not implemented
'''

class BaseGeometry:
    ''' the class raises a an exception'''
    def area(self):
        # raise an error
        raise 'area() is not implemented'
