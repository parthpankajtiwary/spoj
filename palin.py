
def mirrorAndIncrease(string):
	number = int(string)
	if len(string)%2 == 0:
		left = string[:len(string)/2]
		string = left + left[::-1]
		array = [x for x in string]
		while(int("".join(array)) <= int(number)):
			valueOne = int(array[len(array)/2])
			valueTwo = int(array[len(array)/2-1])
			valueOne += 1
			valueTwo += 1
			array[len(array)/2] = str(valueOne)
			array[len(array)/2-1] = str(valueTwo)
		return "".join(array)	
	

	if len(string)%2 != 0:
		left = string[:len(string)/2]
		string = left + string[len(string)/2:len(string)/2+1] + left[::-1]
		array = [x for x in string]

		while(int("".join(array)) <= int(number)):
			value = int(array[len(array)/2])
			value += 1
			array[len(array)/2] = str(value)
		return "".join(array)	
	


t = input()
inputs = []
for x in xrange(t):
	inputs.append(raw_input())

for x in inputs:
	print mirrorAndIncrease(x)	