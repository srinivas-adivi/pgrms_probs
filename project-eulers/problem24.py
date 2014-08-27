#! /usr/bin/python

from permutation import next_big

def problem24():
    n = '0123456789'
    i = 1
    while i<1000000:
        n = next_big(n)
        i = i+1
    return n 

print problem24()

