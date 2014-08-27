from prime import *
from permutation import *

def largestNthPendigital(n):
     p_list = map(lambda n: int(n), permutation(str(n)))
     for n in p_list:
	 if isprime(n):
	     return n

if __name__== "__main__":
    print largestNthPendigital(7654321)
