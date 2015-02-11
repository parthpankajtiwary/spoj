
def calculateMessage(string, m):
	dCipher = []
	print len(string)
	for x in xrange(m):
		for y in xrange(0, len(string), 2*m-1):
			print x+y
			print x+y+1
			# if x == 0 and y == 0:
			# 	dCipher.append(string[0])
			# else:
			# 	dCipher.append(string[x+y])
			# 	dCipher.append(string[x+y+1])	
	
calculateMessage("toioynnkpheleaigshareconhtomesnlewx", 5)				