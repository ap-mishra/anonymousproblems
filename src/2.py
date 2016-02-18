#!/bin/python 

'''

'''
def next_element(s1, s2):
    return s1+s2
def fib1(maxval):
    s = [1, 2]
    idx=0
    while(s[idx]+s[idx+1]<=maxval):
        n = next_element(s[idx], s[idx+1])
        s.append(n)
        idx +=1
    return s

if __name__=='__main__':
    l = fib1(4000000)
    filtered_even = [ s for s in l if s%2 == 0 ]
    print l
    print filtered_even
    print "Sum = " + str(sum(filtered_even))
