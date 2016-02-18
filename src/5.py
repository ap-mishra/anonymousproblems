#!/bin/python
__author__='ashwin'

'''
Problem description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def multiple(n, cap):
    mult=n
    s=[]
    while mult <= cap:
        s.append(mult)
        mult += n


if __name__=='__main__':
    print "something"
    s = range(2,21,1)
    print s
    prod=1
    for i in s:
        prod *= i
    print "Cap : " + str(prod)
    print "Multiples for all numbers : "
    for i in s:
        l = multiple(i, prod)
        print "Multiples for : " + str(i)
        print l


