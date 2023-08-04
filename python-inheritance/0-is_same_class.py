'''
    this is a function that returns true or false if an object is an exact instance of a class.
'''

#a = 1
def is_same_class(obj, a_class):
    ''' check if the object is the exact instance of the class
    '''
    #obj = object
    #a_class = Class
    print(type(obj), type(a_class))
    if type(obj) == a_class:
        return True
    return False


#print(is_same_class(a , int))
