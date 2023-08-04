'''
    a class that raises an error if not implemented
'''

class BaseGeometry:
    ''' the class raises a an exception'''
    def __init__(self):
        #initalize 
        self.self = self

    def area(self):
        # raise an error
        raise 'area() is not implemented'
