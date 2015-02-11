
def numberOfSquares(n):
	squares = (n*(n+1)*(2*n+1))/6
	print squares	

n = -1
sides = []
while(n != 0):
	n = input()
	if n != 0:
		sides.append(n)


for side in sides:
	numberOfSquares(side)		