

t = input()

points = []
for x in xrange(t):
	x, y = map(int, raw_input().split())
	points.append((x, y))

def findNumber(x, y):
	if y == x or y == x - 2:
		if x == y:
			if x%2 != 0 and y%2 != 0:
				number = x + y - 1
			else:
				number = x + y
		else:
			if x%2 == 0 and y%2 == 0:
				number = x + y
			else:
				number = x + y - 1
		print number
	else:
		print "No Number"	

for point in points:
	findNumber(point[0], point[1])						
				