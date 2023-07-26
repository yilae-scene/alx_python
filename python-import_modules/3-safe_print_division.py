# simple function that should divid a and b through
#...try and catch exception


def safe_print_divison(a , b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            print("{} / {} = {}".format(a , b, result))
        else:
            print("Inside result: None")
        return result

