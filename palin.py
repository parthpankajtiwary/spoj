
# def mirror(n, l):
# 	if l%2 == 0:
# 		left = n[:l/2]
# 		array = [left, left[::-1]]
# 		return "".join(array)
# 	else:
# 		left = n[:l/2]
# 		array = [left, n[l/2], left[::-1]]
# 		return "".join(array)

# def increment(n):
# 	numberString = mirror(n, len(n))
# 	p = int(numberString)
# 	if p > int(n):
# 		return p
# 	else:
# 		print "I am in the else clause"
# 		array = [x for x in numberString]
# 		if len(array)%2 == 0:
# 			print "I am satisfying the even clause"
# 			r = (len(n)/2)-1
# 			t = len(n)/2
# 			while(int("".join(array)) <= int(n)):
# 				if int(array[r]) < 9:
# 					array[r] = str(int(array[r])+1)
# 					array[t] = str(int(array[t])+1)
# 				else:
# 					r -= 1
# 					t += 1
# 			return "".join(array)			
				 
			
# t = input()
# inputs = []
# for x in xrange(t):
# 	inputs.append(raw_input())

# for x in inputs:
# 	print increment(x)	


            