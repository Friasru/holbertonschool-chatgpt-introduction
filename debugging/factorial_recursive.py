#!/usr/bin/python3
import sys

def factorial(n):
	"""
Calculates the factorial of a number using recursion.

A factorial is the product of all positive integers less than or equal to n.
For example: 5! = 5 x 4 x 3 x 2 x 1 = 120
Parameters:
	n (int): A non-negative integer to calculate the factorial for

Returns:
	int: The factorial of n
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
