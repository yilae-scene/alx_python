
# a python file that takes a command line argument

import sys


if __name__ == '__main__':

    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    elif n==2:
        print("1 argument:".format(n-1))
        print("1: "+sys.argv[1])
    else:
        print("{} arguments:".format(n-1))
        for x in range(1, n):
            print("{}: {}".format(x, sys.argv[x]))
