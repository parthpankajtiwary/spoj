def findLine(k):
	n = 1
	while((n*(n+1)/2-n) <= k):
		n += 1
	return n-1	

t = input()

inputs = []
for x in xrange(t):
	inputs.append(input())

for x in inputs:
	print findLine(x)
