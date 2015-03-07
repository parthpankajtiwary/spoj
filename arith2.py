def calculate(operations):
	stack = [x for x in operations.split()[:-1]]
	if len(stack) == 3:
		return 


t = input()

for x in xrange(t):
	blank = raw_input()
	operations = raw_input()
	print calculate(operations)