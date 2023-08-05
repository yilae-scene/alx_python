''' 
an empty class that we will implement later
'''
# a meta class that will provide the dir method to BaseGeometry class


class TopMeta(type):
    ''' 
        remove the init__subclass so that BaseGeomety will be without it
    '''

    def __dir__(self):
        attributes = super().__dir__()
        return [x for x in attributes if x != '__init_subclass__']


class BaseGeometry (metaclass=TopMeta):
    ''' 
    there will be some implementations here
    '''

    def __dir__(self):
        attributes = super().__dir__()
        return [x for x in attributes if x != '__init_subclass__']



