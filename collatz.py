#!/usr/bin/python3
import sys

def even(n): return int(n/2)
def odd(n): return int((n*3) + 1)
def isEven(n): return n%2 == 0
def step(n): return  even(n) if isEven(n) else odd(n)

def chain(n):
	result = [n]
	while (n > 1):
		n = step(n)
		result.append(n)
	return result

def reverse(n):
	next = [ int(2*n) ]
	if ((n-1)%3 == 0):
		next.append(int((n-1)/3))
	return next
