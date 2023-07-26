
# a python file that takes a command line argument

import sys


if __name__ == '__main__':

    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    n = len (sys.argv)
    for x in range(1,n):
        print("{}: {}".format(x,sys.argv[x]))

