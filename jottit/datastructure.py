
def sum(L):
	"""return the sum of all elements of a list.
	>>> sum([1, 2, 3, 4, 5])
	15
	>>> sum([])
	>>> sum(["hello", "world"])
	'helloworld'
	"""
	s = L and L[0] or None
	for n in L[1:]:	s = s+n
	return s

def product(L):
    """ return the product of all elements in a given list
    >>> product([])
    >>> product([1, 2, 3, 4, 5])
    120
    >>> product([-1, -3, 5.5])
    16.5
    """
    p = L and 1 or None
    for n in L: p = p*n
    return p

def factorial(N):
	""" return the factorial value of given N
	>>> factorial(5)
	120
	>>> factorial(3)
	6
	>>> factorial(-4)
	Traceback (most recent call last):
		...
	ValueError: n must be >= 0
	>>> factorial(3.14)
	Traceback (most recent call last):
		...
	ValueError: n must be whole number
	"""
	import math
	f = 1
	if not N >= 0:
		raise ValueError("n must be >= 0")
	if math.floor(N) != N:
		raise ValueError("n must be whole number")

	for n in range(N):
		f = f*(n+1)

	return f

def reverse(L):
	""" return the list in reverse order
	>>> reverse([1, 2, 3, 4])
	[4, 3, 2, 1]
	>>> reverse(reverse([1, 2, 3, 4]))
	[1, 2, 3, 4]
	"""

	length = len(L)
	for n in range(length/2): L[n], L[length-n-1] = L[length-n-1], L[n]

	return L

def maximum(L):
    """ return the maximum value among all elements in list
    >>> maximum([1, 2, 3, 4])
    4
    >>> maximum([])
    >>> maximum(['a', 'b', 'c', 'd'])
    'd'
    """
    max = L and L[0] or None
    for n in L[1:]:
    	if max < n: max = n
     
    return max

def minimum(L):
    """return the minimum value among all elements in list
    >>> minimum([1, 2, 3, 4])
    1
    >>> minimum([])
    >>> minimum(["sri", "nivas"])
    'nivas'
    """
    min = L and L[0] or None
    for n in L[1:]:
    	if min > n: min = n

    return min

def cumulative_sum(L):
    """return cumulative sum of a list
    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([4, 3, 2, 1])
    [4, 7, 9, 10]
    """
    sum = L and [L[0]] or []
    for val in L[1:]: sum.append(sum[-1]+val)
    return sum

def cumulative_product(L):
    """ return cumulative product of a list
    >>> cumulative_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> cumulative_product([4, 3, 2, 1])
    [4, 12, 24, 24]
    """
    product = L and [L[0]] or []
    for val in L[1:]:   product.append(product[-1]*val)
    return product

def lensort(L):
    """return list of sorted words by length then by letters of 
    given list of words
    >>> lensort(['sri', 'nivas', 'vijay', 'rama', 'naga'])
    ['sri', 'rama', 'naga', 'nivas', 'vijay']
    >>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'lisp', 'ocaml', 'smalltalk', 'ruby'])
    ['c', 'perl', 'java', 'lisp', 'ruby', 'ocaml', 'python', 'haskell', 'smalltalk']
    """
    L.sort(key=lambda x: len(x))
    return L

def extsort(L):
    """return sorted list of files based on extension
    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
    >>> extsort(['a.c', 'a.z.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.z.py', 'b.py', 'bar.txt', 'foo.txt']
    """
    split_at_dot = [filename.rsplit('.',1) for filename in L]
    split_at_dot.sort(key=lambda x: x[1])
    return ['.'.join(list) for list in split_at_dot]

def zip(a, b):
	"""
	>>> zip([1, 2, 3], ["a", "b", "c"])
	[(1, 'a'), (2, 'b'), (3, 'c')]
	"""
	return [(a[i],b[i]) for i in range(len(a)<len(b) and len(a) or len(b))]

def map(func, list):
	"""
	>>> def square(x): return x * x
	...
	>>> map(square, range(5))
	[0, 1, 4, 9, 16]
	"""
	return [func(x) for x in list]

def filter(func, list):
    """
    >>> def square(x): return x * x
    ...
    >>> filter(square, range(5))
    [1, 2, 3, 4]
    >>> def even(x): return x%2 == 0
    ...
    >>> filter(even, range(10))
    [0, 2, 4, 6, 8]
    """
    return [x for x in list if func(x)]

def triplets(n):
    """ returns a list of triplets such that sum of first two elements of 
        the triplet equals the third element using numbers below n.
        Note:(a, b, c) and (b, a, c) represent same triplet
    >>> triplets(5)
    [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
    """
    return [(a, b, a+b) for a in range(1, n)for b in range(a, n-1) if a+b < n]

def enumerate(list):
    """ returns a list of tuples containing (index,item) for each item in 
        the list.
    >>> enumerate(["a", "b", "c"])
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> for index, value in enumerate(["a", "b", "c"]):
    ...     print index, value
    0 a
    1 b
    2 c
    """
    return [(i, list[i]) for i in range(len(list))]

def array(row, col):
    """ return list containing 'col' lists which are initialized by row of 
        None i.e return two dimentional array of given parameters
    >>> a = array(2, 3)
    >>> a
    [[None, None, None], [None, None, None]]
    >>> a[0][0] = 5
    >>> a
    [[5, None, None], [None, None, None]]
    """
    return [[None for i in range(col)] for i in range(row)]

def parse_csv(csvfile):
    """
    >>> print open('a.csv').read()
    a,b,c
    1,2,3
    2,3,4
    3,4,5
    <BLANKLINE>
    >>> parse_csv('a.csv')
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
    """
    return [line.strip().split(',') for line in open(csvfile).readlines()]

def parse(filename, sep, comment):
    """
    >>> print open('a.txt').read()
    # elements are separated by ! and comment indicator is #
    a!b!c
    1!2!3
    2!3!4
    3!4!5
    <BLANKLINE>
    >>> parse('a.txt', '!', '#')
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
    """
    return [line.strip().split(sep) for line in open(filename).readlines()if not line.startswith(comment)]

def mutate(word):
    """
    >>> words = mutate('hello')
    >>> 'helo' in words
    True
    >>> 'cello' in words
    True
    >>> 'helol' in words
    True
    >>> words = mutate('')
    >>> len(words)
    26
    """
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    length = len(word)
    result = genarate_insertion(word, lowercase)
    result.extend(genarate_replace(word, lowercase))
    result.extend(genarate_deletion(word))
    result.extend(genarate_swap(word))
    return result

def genarate_insertion(word, lowercase):
    """ return list of all words which are genarate by inserting every 
        letter of lowercase in every position of word
    >>> genarate_insertion('sri', 'ab')
    ['asri', 'sari', 'srai', 'bsri', 'sbri', 'srbi']
    """
    return [insert(word, i, ch)for ch in lowercase for i in range(len(word) or 1)]

def genarate_replace(word, lowercase):
    """ return list of all words which are genatate by replace every letter
         of word by every letter of lowercase
    >>> genarate_replace('sri', 'ab')
    ['ari', 'bri', 'sai', 'sbi', 'sra', 'srb']
    """
    return [replace(word, i, ch) for i in range(len(word))for ch in lowercase]
    
def genarate_deletion(word):
    """ return list of all words which are genarate by delete each letter 
        of given word
    >>> genarate_deletion('sri')
    ['ri', 'si', 'sr']
    """
    return [delete(word, i) for i in range(len(word))]

def genarate_swap(word):
    """ return list of all words which are genarate by swap consecutive 
        letters in given word
    >>> genarate_swap('sri')
    ['rsi', 'sir']
    """
    return [swap(word, i, i+1)for i in range(len(word)-1)]

def insert(word, index, ch):
	"""return word which is getting by insert char at before index place
		by given char in given word
	>>> insert('hello', 1, 'a')
	'haello'
	>>> insert('hello', 4, 'z')
	'hellzo'
	"""
	list1 = list(word)
	list1.insert(index, ch)
	return ''.join(list1)

def replace(word, i, ch):
	"""return word which is getting by replace char at given index 
		by given char in given word
	>>> replace('hello', 2, 'h')
	'hehlo'
	>>> replace('hello', 0, 'c')
	'cello'
	"""
	list1 = list(word)
	list1.pop(i)
	list1.insert(i, ch)
	return ''.join(list1)
		
def swap(word, index1, index2):
	""" return word which is getting by swap char at given indies in 
		given word
	>>> swap('hello', 1, 2)
	'hlelo'
	>>> swap('hello', 2, 3)
	'hello'
	"""
	length = len(word)
	if 0<=index1<length and 0<=index2<length:
		list1 = list(word)
		list1.insert(index2, list1.pop(index1))
		return ''.join(list1)

def delete(word, index):
	"""return a word after delete a char at given index in given word 
	>>> delete('hello', 1)
	'hllo'
	>>> delete('hello', 3)
	'helo'
	"""
	list1 = list(word)
	list1.pop(index)
	return ''.join(list1)

def nearly_equal(str1, str2):
    """ return True if str1 can be genrated by a sigle muatation on str2 otherwise False
    >>> nearly_equal('python', 'perl')
    False
    >>> nearly_equal('perl', 'pearl')
    True
    >>> nearly_equal('python', 'jython')
    True
    >>> nearly_equal('man', 'woman')
    False
    """
    return str1<str2 and str2 in mutate(str1) or str1 in mutate(str2)

def anagrams(words_list):
    """ return list which contain anagrams lists of given list of words 
    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node', 'ant', 'tan'])
    [['ant', 'tan'], ['done', 'node'], ['eat', 'ate', 'tea'], ['soup']]
    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['done', 'node'], ['eat', 'ate', 'tea'], ['soup']]
    """
    dir = {}
    for word in words_list:
        list1 = list(word)
        list1.sort()
        key = ''.join(list1)
        dir.setdefault(key, []).append(word)

    return dir.values()


def valuesort(dict):
	""" write function valuesort to sort values of a dictionary based on
    the key.
	>>> valuesort({'x': 1, 'y': 2, 'a': 3})
	[3, 1, 2]
	"""
	items = dict.items()
	items.sort(key=lambda x: x[0])
	return [value for key, value in items]

def invertdict(dict):
	''' Write a function invertdict to interchange keys and values in a 
    dictionary For simplicity, assume that all values are unique.
	>>> invertdict({'x': 1, 'y': 2, 'z': 3})
	{1: 'x', 2: 'y', 3: 'z'}
	'''
	result = {}
	for key, value in dict.items():
		result[value] = key
	return result

if __name__ == "__main__":
	import doctest
	doctest.testmod()
