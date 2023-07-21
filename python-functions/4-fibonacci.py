
# write a fibonacci function to
def fibonacci_sequence(n):
    # for numbers below or equal to n
    if n <= 0:
        return []
    # for input number 1
    elif n == 1:
        return [0]
    # for fibonacci numbers always start with 0 and 1
    else:
        # constant initialization of starting_list of fibonacci
        fib_sequence = [0, 1]

        for i in range(2 , n):
            # make a variable that holds the fibonacci result
            append_list = fib_sequence[i - 2] + fib_sequence[i - 1]
            # append the result ot starting_list
            fib_sequence.append(append_list)
    return fib_sequence



