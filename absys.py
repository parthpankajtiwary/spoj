t = input()
answers = []


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def findMachula(input):
	array = [x for x in input.split()]
	if not isInt(array[0]):
		array[0] = str(int(array[4]) - int(array[2]))
	else:
		if not isInt(array[2]):
			array[2] = str(int(array[4]) - int(array[0]))
		elif not isInt(array[4]):
			array[4] = str(int(array[0]) + int(array[2]))
	answers.append(" ".join(array))					
	
for x in xrange(t):
	blankLine = raw_input()
	input = raw_input()
	findMachula(input)

for x in answers:
	print x	