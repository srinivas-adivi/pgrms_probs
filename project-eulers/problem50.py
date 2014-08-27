import prime

def problem50():
    primesList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    prime.primesBelow_fast(1000000, primesList)
    primesDict = dict.fromkeys(primesList)
    
    resultDict = {}

    length, count, limit = len(primesList), 1, primesList[-1]
    currentList = primesList[:]
    diffList = [0]*length
    while length:
	result = [x+y-z for x,y,z in zip(currentList[:-1],currentList[1:], diffList) if x+y-z<limit]
	length, count = len(result), count+1
	diffList, currentList = currentList[1:length], result[:]
	if count%2:
	    resultDict[count] = [n for n in result[1:] if primesDict.has_key(n)]
	else:
	    n = result and result[0] or 0
	    resultDict[count] = primesDict.has_key(n) and [n] or []
    
    R = filter(lambda x: resultDict[x], resultDict.keys())
    R.sort()
    return R[-1], resultDict[R[-1]]
print problem50()

