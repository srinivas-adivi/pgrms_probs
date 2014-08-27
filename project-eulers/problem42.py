
def problem42():
    '''http://projecteuler.net/index.php?section=problems&id=42'''
    cap_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cap_letters_list = list(cap_letters)
    index = range(1, 27) 
    letter_values = dict(zip(cap_letters, index))
    
    triangle_words = []
    #Getting words as list from csv file
    text = open('problem42.txt', 'r').read()
    words_list = [word.strip('"') for word in text.strip().split(',')]
    no_of_words = len(words_list)
    
    #Make a dictanory having word value(SKY=19+12+25=55) 
    #and list of words as key and values respectively 
    word_values = {}
    for word in words_list:
	word_value = sum(map(lambda x: letter_values[x], list(word)))
	word_values.setdefault(word_value,[]).append(word)
    
    limit = max(word_values)
    #Getting sequence of trianlge numbers upto the 'limit'
    value, triangle_value, triangle_numbers = 1, 1, []
    while triangle_value < limit+1:
	triangle_numbers.append(triangle_value)
	value = value+1
	triangle_value = triangle_value+value
    
    no_triangle_words = 0
    for key in word_values:
	if key in triangle_numbers:
	    no_words = len(word_values[key])
	    no_triangle_words = no_triangle_words+ no_words
	
    return no_triangle_words

print problem42()
