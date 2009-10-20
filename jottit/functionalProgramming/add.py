#! /usr/bin/python

def increment(n): return n+1
def decrement(n): return n-1

def add(a, b):
    """ return value of addition of given two num by using increment and decrement
    >>> add(1, 2)
    3
    >>> add(-2, 4)
    2
    >>> add(2, -3)
    -1
    >>> add(-2, -1)
    -3
    """
    if b == 0:
        return  a
    if a == 0:
        return b
    if a>0 or b<0:
        return add(decrement(a), increment(b))
    else:
        return add(increment(a), decrement(b))
     
if __name__=="__main__":
    import doctest
    doctest.testmod()

