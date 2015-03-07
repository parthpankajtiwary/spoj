t = input()
for x in range(t):
	n, m = map(int, raw_input().split())
	a = [int(x) for x in raw_input().split()]
	a.sort()
	s = 0
	for x in range(m):
		if a[x] < 0:
			s += abs(a[x])
	print s		