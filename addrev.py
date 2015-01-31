t = input()

def calResult(a, b):
	arrayA = [x for x in a]
	arrayB = [x for x in b]
	arrayA.reverse()
	arrayB.reverse()
	return str(int("".join(arrayA)) +  int("".join(arrayB)))[::-1]

answers = []
for x in xrange(t):
	a, b = map(str, raw_input().split())
	answers.append(int(calResult(a, b)))

for x in answers:
	print x	
