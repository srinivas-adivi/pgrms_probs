
def problem42():
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    index = range(1,27)
    
    letter_values = dict(zip(letters, index))
    
    triangle_words = []
    text = open('problem42.txt', 'r').read()
    words_list = [word.strip('"') for word in text.strip().split(',')]
    no_of_words = len(words_list)

    word_values = {}
    for word in words_list:
	word_value = sum(map(lambda x: letter_values[x], list(word)))
	word_values.setdefault(word_value,[]).append(word)
    
    limit = max(word_values)
    print limit
    value, triangle_value, triangle_numbers = 1, 1, []
    while triangle_value < limit+1:
	triangle_numbers.append(triangle_value)
	value = value+1
	triangle_value = triangle_value+value
    
    no_triangle_words = 0
    for key in word_values:
	if key in triangle_numbers:
	    no_words = len(word_values[key])
	    print 'key', key
	    print 'no_words', no_words
	    no_triangle_words = no_triangle_words+ no_words#len(word_values[key])
	
    return no_triangle_words

print problem42()
