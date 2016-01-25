import sys

def fizzbuzz(n):

    """
    fizzbuzz.py python program accepts an integer n from the command line.

    Pass this integer to a function called fizzbuzz. The fizzbuzz function should then iterate from 1 to n.

    ith number is a multiple of two, print “fizz”,
    ith number is a multiple of three print “buzz”
    ith number is a multiple of both print “fizzbuzz”
    else print the value


    """

    if n % 2 == 0 and n % 3 == 0
        return 'fizzbuzz'
    elif n % 2 == 0:
        return 'fizz'
    elif n % 3 == 0:
        return 'buzz'
    else:
        return str(n)

if __name__ = '__main__':
    n = int(sys.arg[1])
    print fizzbuzz(n)
