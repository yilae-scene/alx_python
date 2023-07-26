# simple function that should divid a and b through
#...try and catch exception


def safe_print_divison(a , b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        if result!=None:
            print("Inside result: {}".format(result))
            print("{:d} / {:d} = {}".format(a , b, result))
        else:
            print("Inside result: {}".format(result))
            print("{:d} / {:d} = {}".format(a , b, result))

