# simple function that should divid a and b through
#...try and catch exception


def safe_print_divison(a , b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a , b, result))


