'''
    a class that raises an error if not implemented
'''

class BaseGeometry:
    def __init__(self):
        self.self = self

    def area(self):
        raise 'area() is not implemented'
