#!/usr/bin/python3
import sys
import collatz

if (len(sys.argv) > 1):
	num = int(sys.argv[1])
else:
	num = int(input("Start at: "))

print (collatz.chain(num))
