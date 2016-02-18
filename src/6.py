#!/bin/python
import numpy as np
__author__='ashwin'

'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''
def sumofsquares(no):
    l = [ np.power(s,2) for s in range(1,no+1,1)]
    return sum(l)

def squaresofsum(no):
    l = [ s for s in range(1, no+1, 1)]
    return np.power(sum(l),2)

if __name__=='__main__':
    print "something"

    number  = 100
    tot1 = sumofsquares(number)
    tot2 = squaresofsum(number)
    print "Total 1 : " + str(tot1)
    print "Total 2 : " + str(tot2)
    print "Difference : " + str(tot2 - tot1)
    #do something
