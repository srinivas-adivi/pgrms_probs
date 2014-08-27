
def count_change(amount, denominations):
    """ return the number of ways to change any given amount.
         Available coins are also passed as argument to the function.
    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292
    >>> count_change(200, [1, 2, 5, 10, 20, 50, 100, 200])
    73682
    """
    if amount == 0:
        return 1
    elif denominations == []:
        return 0
    else:
        count = 0
        n = amount/denominations[0]
        for i in range(n+1): 
            change = denominations[0]*i
            count += count_change(amount-change, denominations[1:])
        return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
