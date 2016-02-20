#!/bin/python
__author__='ashwin'

'''
Problem description:

'''

if __name__=='__main__':
    a = 2 ** 1000
    x = str(a)
    print x
    print "Length = " + str(len(x))
    sum1=0
    for i in range(0,len(x)):
        print x[i]
        sum1 += int(x[i])
    print "-----------SUM--------------"
    print sum1

