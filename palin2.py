def nextPalin(n):
	



t = input()
answers = []
for x in xrange(t):
	answers.append(nextPalin(input()))

for x in answers:
	print x		