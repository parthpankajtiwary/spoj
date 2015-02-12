
def countMoves(candies):
	if sum(candies)%len(candies) != 0:
		print -1
	else:
		average = sum(candies)/len(candies)
		steps = 0
		for x in candies:
			if x < average:
				steps += (average - x)
		print steps
		
inputs = []
while(True):
	n = input()
	if n == -1:
		break
	else:
		tempArray = []
		for x in xrange(n):
			tempArray.append(input())
		inputs.append(tempArray)

for x in inputs:
	countMoves(x)			