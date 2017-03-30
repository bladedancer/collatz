#!/usr/bin/python3
import sys
import collatz
import pydot

chains = list();

def reverseCollatz(cur, end):
	n = cur[len(cur)-1]
	next = collatz.reverse(n)
	for val in next:
		if (cur.count(val) > 0):
			# Loop
			continue
		elif (val%2 == 0 and val/2 != n):
			# Not a valid link (even nums divide by 2 so val has to be 2*n if even)
			continue;
		elif (val > end):
			# End of the chain
			cur.append(val);
			chains.append(list(cur))
			cur.pop();
			continue;
		else:
			cur.append(val);
			reverseCollatz(cur, end)
			cur.pop();


if (len(sys.argv) > 1):
	num = int(sys.argv[1])
else:
	num = int(input("Stop when greater than: "))

reverseCollatz([1], num);
for chain in chains:
	print(chain);

# Draw it
graph = pydot.Dot(graph_type='graph')

links = list()
for chain in chains:
	for i in range(1, len(chain)):
		link = str(chain[i-1]) + '->' + str(chain[i])
		if (links.count(link) > 0):
			# Already linked
			continue
		else:
			links.append(link)
		# Draw it
		edge = pydot.Edge(str(chain[i-1]), str(chain[i]))
		graph.add_edge(edge)

graph.write_png('collatz.png')
