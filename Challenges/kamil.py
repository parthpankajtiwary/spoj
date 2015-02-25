t = []
for x in range(10):
	t.append(raw_input())
l = ["D", "T", "F", "L"]
for x in t:
	c = 0
	for y in l:
		if y in x:
			c += x.count(y)
	print 2**c

