from string import ascii_lowercase

def RPN(n):
	precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
	alphabet = [x for x in ascii_lowercase]
	expression = []
	stack = []
	for x in n:
		if x in alphabet:
			expression.append(x)
		elif x == "(":
			stack.append(x)
		elif x == ")":
			value = ""
			while(value != "("):
				value = stack.pop()
				expression.append(value)
			stack.pop()
		elif x in precedence:
			if(len(stack) != 0):
				if precedence[x] < precedence[stack[-1]]:
					expression.append(x)
				else:
					while(precedence[x] <= precedence[stack[-1]]):
						expression.append(stack.pop())
				stack.append(x)
			else:
				expression.append(x)			
	print expression			
	return "".join(expression)



t = input()
inputs = []
for x in xrange(t):
	inputs.append(raw_input())

for x in inputs:
	print RPN(x[1:-1])	



