'''
    this is a function that returns true or false if an object is an exact instance of a class.
'''

def is_same_class(obj, a_class):
    ''' check if the object is the exact instance of the class
    '''
    #obj = object
    #a_class = Class
    if type(object) == type(a_class):
        return True
    return False


