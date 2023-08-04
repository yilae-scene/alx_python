'''
    the following function checks if the object is an instance of a class
'''

def is_kind_of_class(obj, a_class):
    ''' the function takes object and class 
        checks whether the object is instance of class
    '''
    #obj = object
    #a_class = class
    if isinstance(obj, a_class):
        return True
    return False

