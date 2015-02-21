def lastDig(a, b):
    if b == 0:
        return 1
    if b%4 == 0:
        return str(a**4)[-1]
    if b%2 == 0 and b%4 != 0:
        return str(a**2)[-1]
    if b%4 == 1:
        return str(a**1)[-1]
    if b%4 == 3:
        return str(a**3)[-1]        

t = input()
answers = []
for x in xrange(t):
    a, b = map(int, raw_input().split())
    answers.append(lastDig(a, b))

for x in answers:
    print x    