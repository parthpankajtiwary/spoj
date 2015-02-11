
def determine(a, b, c):
	diffOne = c-b
	diffTwo = b-a
	if diffOne == diffTwo:
		print "AP",
		print c + diffOne
	else:
		r = c/b
		print "GP",
		print c*r

inputs = []
while(True):
	t = raw_input()
	if t == "0 0 0":
		break
	else:
		inputs.append(t)	

for x in inputs:
	a, b, c = map(int, x.split())
	determine(a, b, c)

	