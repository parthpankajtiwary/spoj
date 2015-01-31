

t = input()

def factorial(a):
	result = 1
	while(a >= 1):
		result *= a
		a -= 1
	return result

answers = []	
for x in xrange(t):
	a = input()
	answers.append(factorial(a))

for x in answers:
	print x	