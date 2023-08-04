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
