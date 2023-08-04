''' 
an empty class that we will implement later
'''


class BaseGeometry (object):
    ''' there will be some implementations here
    # '''
    def __dir__(self):
        attributes =object.__dir__()
        return [x for x in attributes if x != '__init_subclass__']
  

# print(dir(BaseGeometry))
