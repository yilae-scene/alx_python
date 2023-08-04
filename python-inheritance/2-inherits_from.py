'''
    the following function checks if the object is an instance of a class
'''


def inherits_from(obj, a_class):
    ''' the function takes object and class checks whether the object is instance 
    of class'''
    
    # obj = object
    # a_class = class
    if isinstance(object, a_class) and issubclass(a_class, b_class):
        return True
    return False
