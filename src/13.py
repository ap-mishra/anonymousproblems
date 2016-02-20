#!/bin/python
__author__='ashwin'

'''
Problem description:

'''
def read_file(filename):
    s = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            s.append(int(line))
    return s

if __name__=='__main__':
    #do something
    print "something"

    #read from file
    arr = read_file("../data/13.dat")
    print arr

    print "Sum of numbers"
    s1=sum(arr)
    print s1

