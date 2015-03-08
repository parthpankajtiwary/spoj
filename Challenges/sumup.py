for x in range(input()): 
	s=0 
	for y in range(1,input()+1): s+=float(y)/((y**2+1)**2-y**2)
	print"%.5f"%s	