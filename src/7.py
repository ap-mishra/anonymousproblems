#!/bin/python
__author__='ashwin'

'''
Problem description:
'''

def check_factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

if __name__=='__main__':
    n = 10001
#    print n
#    print check_factors(n)
#    print "factors of : " + str(n) 
    i = 2
    count = 1
    while(count <= 10001):
        l = check_factors(i)
        length = len(l)
        if length<=2:
            print "Prime number : " + str(count) + ", is " + str(i)
            count += 1
        i += 1

    print check_factors(n)
