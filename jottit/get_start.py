
#PROBLEM1

#Ans: a = 1, b = 1
#Because, first of all, all expressions are evaluate and then assign to 
#corresponding names

def code1():
    'example code1 which shows expression will evaluate frist'
	""" return values of 'a', 'b'.
	>>> code1()
	(1, 1)
	"""
	a, b = 0, 1
	a, b = b, a+b
	
    return a, b

#PROBLEM2
def code2():
    'example code2' 
    """return value of b.
	>>> code2()
	1
	"""
	a = 1
	b = a
	a = 2
	return b

#PROBLEM3

#Ans: no error. it will work smothly.
#Because python will not bother about values of variables.
#first it will check whether is there any wrong in syntax.
#Then it will try to assign the values of variable whenever that 
#variable is used.
#But in this case there is no error in syntax and no need of the value 
#of 'y'because never go to the 'else' statement

def code3():
    'example code3'
	"""print the value of x
	>>> code3()
	2
	"""
	x = 2
	if x == 2:
	    print x
	else:
		print y

#PROBLEM4
#Ans: it will give syntax error.
#Because first it will check whether is there any wrong in syntax.
#in this case syntax error in line 11 

#def code4():
#	x = 2
#	if x == 2:
#       print x
#	else:
#		x +


#PROBLEM5

#Ans: 3, 2 times +, * operations respectively performed to evaluate 
#the aboue expression.

def sum_of_squares(a, b):
	"""
	>>> sum_of_squares(1+1, 1+2)
	13
	"""
	return a*a+b*b

#PROBLEM6
def absolute(n):
	""" return the absolute value of given number
	>>> absolute(4)
	4
	>>> absolute(-3)
	3
	>>> absolute(0)
	0
	"""
	return n < 0 and -n or n

#PROBLEM7
def minimum(a, b):
	""" return the minimum of given 'a','b' values.
	>>> minimum(2, 3)
	2
	>>> minimum(3, -2)
	-2
	"""
	return a < b and a or b

def maximum(a, b):
	""" return the maximum of given 'a','b' values.
	>>> maximum(2, 3)
	3
	>>> maximum(3, -2)
	3
	>>> maximum("sri", "nivas")
	'sri'
	"""
	return a < b and b or a

#PROBLEM9	

#Ans: no problem in newif function. i did not find any example to 
#discreminate between if and newif.

def newif(c, a, b):
	if c:
		return a
	else:
		return b

def absolute(a):
	""" return the absolute value of given 'a'.
	>>> absolute(4)
	4
	>>> absolute(-3)
	3
	>>> absolute(0)
	0
	"""
	return newif(a>0, a, -a)

#PROBLEM10

def f(x): return x + x

def g(): 
	""" 
	>>> g()
	10
	"""
	return f(5)

def f(x): return x * x

#PROBLEM11
def swap():
    global a
    global b
    a, b = b, a
"""
>>> a, b = 1, 2
>>> swap()
>>> print a, b
2 1
"""
a = 1
b = 2
swap()


if __name__ == "__main__":
	import doctest
	doctest.testmod()

