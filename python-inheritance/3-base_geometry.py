''' 
an empty class that we will implement later
'''


class BaseGeometry:
    ''' there will be some implementations here
    # '''
    def __dir__(cls):
        attributes = super().__dir__()
        return [x for x in attributes if x != '__init_subclass__']
  

