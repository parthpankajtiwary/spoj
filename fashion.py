answers = []
def hotnessBonds(a, b, n):
	aArray = map(int, a.split())
	bArray = map(int, b.split())
	aArray.sort()
	bArray.sort()
	sum = 0
	for x in xrange(n):
		sum += aArray[x]*bArray[x]
	answers.append(sum)	


t = input()

for x in xrange(t):
	n = input()
	a = raw_input()
	b = raw_input()
	hotnessBonds(a, b, n)

for x in answers:
	print x	

