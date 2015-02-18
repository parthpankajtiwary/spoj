import sys
answers = []
def maxAmount(n):
	if n < 12:
		return n
	else:
		return maxAmount(n/2) + maxAmount(n/3) + maxAmount(n/4)

while(True):
	a = raw_input()
	if a == "":
		break
	else:
		answers.append(maxAmount(int(a)))	

for x in answers:
	print x	



