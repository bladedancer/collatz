#!/usr/bin/python3
import sys
import collatz

if (len(sys.argv) > 1):
	num = int(sys.argv[1])
else:
	num = int(input("Up to: "))

maxLen = 1;
maxNum = 1;
for i in range(1, num):
	chain = collatz.chain(i)
	chainLen = len(chain)
	maxNum = i if chainLen > maxLen else maxNum
	maxLen = chainLen if chainLen > maxLen else maxLen

	# print(str(i) + ':' + str(chainLen))

print('Max: ' + str(maxNum) + ':' + str(maxLen))
