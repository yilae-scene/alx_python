
# Remove all c from a string.

def no_c(my_string):
    new_string = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return new_string



