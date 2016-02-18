#!/bin/python

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


if __name__ == '__main__':
    l = range(1,1000,1)
    s = [m for m in l if m%3 == 0 or m%5 == 0]
    print l
    print s
    print "Sum = " + str(sum(s))
