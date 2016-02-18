#!/bin/python
__author__='ashwin'

import time

'''
Problem description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

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

def check_factors_vectorized(n):
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def check_factors(no):
    i=1
    count=0
    s=[]
    while(i <= no/2):
    #    print "Iteration : " + str(i)
        if(no%i == 0):
            count+=1
#            if (check_prime(i)==1):
#                s.append(i)
        i+=1
        if(i%10000000==0):
            print "Iteration : " + str(i)
    return count, s

if __name__=='__main__':
    start_time = time.time()

    num = 600851475143
    print "Number we are checking for :" + str(num)
#    l, s = check_factors(num)
    s = check_factors_vectorized(num)
#    print "Total factors : " + str(l)
    print "Prime factors : "
    print s

    print "----Max of prime factors------"
    print max(s)
    print sorted(s)
    time_taken = time.time() - start_time
    m, s = divmod(time_taken, 60)
    print "Total time taken = " + "%02d:%02d" % (m, s)
    print "------------ Final value -------------"
    val = check_prime(6857)
    print val
