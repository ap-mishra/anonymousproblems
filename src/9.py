#!/bin/python
__author__='ashwin'
import numpy as np

'''
Problem description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

if __name__=='__main__':
    #do something
    s = []
    n=1000
    for a in range(1,n+1):
        for b in range(1,n+1):
            if (n-a-b>=1):
                ar = sorted([a,b,n-a-b])
                print ar
                print "elements : "+str(ar[0]) + str(ar[1]) + str(ar[2])
                s.append(ar)
    print sorted(s)

    for tuple in s:
        print "Tuple = : " + str(tuple)
        max1 = tuple[2]
        mid1 = tuple[1]
        min1 = tuple[0]
        print "Components : max : "+ str(max1) + ", mid = " + str(mid1) + ", min1 = " + str(min1)
        if (np.power(max1,2) == np.power(min1,2) + np.power(mid1,2)):
            print "Success ...."
            print tuple
            exit(0)







#    for a in x:
#        b = a + 1
#        while(b>a):
#            c=1000-a-b
#            print a, b, c
#            while(c>b):
#                if (np.power(c,2) == np.power(a,2) + np.power(b,2)):
#                    print "a = " + str(a)
#                    print "b = " + str(b)
#                    print "c = " + str(c)
#                c += 1
#            b += 1
#        a += 1
                    
