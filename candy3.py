answers = []
def possible(n):
	if sum(n)%len(n) == 0:
		answers.append("YES")
	else:
		answers.append("NO")


t = input()			
for x in xrange(t):
	waste = raw_input()
	n = input()
	array = []
	for x in xrange(n):
		array.append(input())
	possible(array)	

for x in answers:
	print x
