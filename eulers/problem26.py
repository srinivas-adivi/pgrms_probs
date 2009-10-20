def problem26():
    """http://projecteuler.net/index.php?section=problems&id=26"""
    L = range(2, 1000)
    result = []
    for n in L:
        remainders = [1]
        divident = 10
        while divident:
            if divident < n:
                #remainders.append(divident)
                divident = divident * 10
            else:
                quoient, divident = divmod(divident, n)
                if divident in remainders:
                    index = remainders.index(divident)
                    result.append((n, len(remainders)- index))
                    break
                else:
                    remainders.append(divident)
    result.sort(key=lambda (n, c): c)
    print result[-1]
problem26()
