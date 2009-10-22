from permutation import *

def problem43():
    '''http://projecteuler.net/index.php?section=problems&id=43'''
    total, permutationsList = 0, permutation('987643210')
    for n in permutationsList:
        n = n[:5]+'5'+n[5:]
        if int(n[7:10])%17==0 and int(n[6:9])%13==0 and\
        int(n[5:8])%11==0 and int(n[4:7])%7==0 and\
        int(n[2:5])%3==0 and int(n[1:4])%2==0:
	    total += int(n)
    return total

print problem43()
