#!/bin/python
__author__='ashwin'

'''
Problem description:

'''
def check_factors_vectorized(n):
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def check_prime(no):
    i=1
    count=0
    while(i <= no):
        if(no%i == 0):
            count += 1
        i+=1
        if (count>2):
            break
    
    if (count>2):
        return 0
    else:
        return 1 

if __name__=='__main__':
    print "something"
    i=3
    val=0
    s=[]
#    threshold = 2000000
    threshold = 20000
    while (val<threshold-1):
#        if len(check_factors_vectorized(i))==2:
        if check_prime(i):
            #print "Checking val " + str(i)
            s.append(i)
            val += 1
        print "Prime no. count :" + str(val)
        i += 2

    s.append(2)
    print len(s)
    print s
    print "---------"
    print sum(s)
