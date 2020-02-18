# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	fact=1
	if type(n)!= int:
		return(None)
	if n<0:
		raise ValueError
	while(n>0):
		fact=fact*n
		n-=1
	return(fact)

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta=(b**2)-(4*a*c)
	if delta < 0:
		return ()
	if delta==0:
		return ((-b)/2*a,)
	if delta>0:
		return (((-b + sqrt(delta))/2*a),((-b - sqrt(delta))/2*a))

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""

	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, -2, 1))
	print(integrate('x ** 2 - 1', -1, 1))
