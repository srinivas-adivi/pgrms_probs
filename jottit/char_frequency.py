
def char_frequency(string):
	"""Returns frequency of each char given string.
	>>> char_frequency(['a', 'b', 'a'])
	{'a': 2, 'b': 1}
	"""
	frequency = {}
	for ch in string:
	    frequency[ch] = frequency.get(ch, 0) + 1
	return frequency

def main(filename):
	frequency = char_frequency(open(filename).read())
	items = frequency.items()
	items.sort(key=lambda x:x[1])
	for ch, count in items[::-1]:
		print repr(ch), count

if __name__ == "__main__":
	import doctest
	import sys

	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print "USAGE: 'python char_frequency.py filename'"

	doctest.testmod()
		
