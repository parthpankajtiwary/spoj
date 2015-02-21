
inputs = []
flag = True
while(flag):
	input = raw_input()
	if input == "0.00":
		flag = False
	else:
		inputs.append(input)	


for x in inputs:
	if float(x) <= 0.5:
		print "1 card(s)"
	else:
		hang = 0.5
		n = 2.0
		while(hang < float(x)):
			hang += 1.0/(n+1)	
			n += 1.0
		print "%s card(s)" % str(int(n-1))