#!/bin/python
__author__='ashwin'

'''
Problem description:
'''
#Smallest number : 10000
#Largest number : 998001

def check_factors_vectorized(n):
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def check_elements(n, length, idx):
    flag=0
    if (n[idx] != n[length - idx]):
        return 0
    if ((length+1)%2 != 0):
        if (idx == length - idx):
            return 1

    if ((length+1)%2 == 0):
        if (idx == length - idx - 1):
            return 1
    return check_elements(n, length, idx + 1)


def lenDigits(x): 
    """
    Assumes int(x)
    """
    x = abs(x)
    if x < 10:
        return 1
    return 1 + lenDigits(x / 10)

def check_palindrome(n):
    length = lenDigits(n)
    if (check_elements(str(n), length - 1, 0)):
            print "Found the largest pallindrome : " + str(n)
            
            factors = check_factors_vectorized(n)
            factors = list(factors)
            return n

if __name__=='__main__':
    # do something
    print "something"

    nos = range(999,99,-1)
    l=[]
    for i in nos:
        for j in nos:
            prod = i*j
            l.append(check_palindrome(prod) )
    print "--------------------------"
    print l
    print "--------------------------"
    print max(l)
