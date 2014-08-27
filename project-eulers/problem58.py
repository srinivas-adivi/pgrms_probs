import prime

def problem58():
    numOnDiagonal, width, noOfPrimes = 13, 7, 8 
    while noOfPrimes*10 > numOnDiagonal:
	nextWidth, square = width+2, width*width
	nextSquare = nextWidth*nextWidth
	result = xrange(square+width+1, nextSquare+1, width+1)
	noOfPrimes = noOfPrimes+ len(filter(lambda n: prime.isprime(n), result))
	numOnDiagonal = numOnDiagonal+4
	width = nextWidth
    return width
print problem58()
