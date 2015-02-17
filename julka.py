def apples(t, m):
	x = (t-m)/2
	return x+m, x

answers = []
for x in xrange(10):
	t = input()
	m = input()
	answers.append(apples(t, m))

for x in answers:
	print x[0]
	print x[1]


