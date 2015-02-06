from math import sqrt
 
def FindPrimes(limit):
    isPrime = {}
 
    isPrime[1] = False
    for i in xrange(2, limit + 1):
        isPrime[i] = True
 
    checkLimit = int(sqrt(limit)) + 1
    for i in xrange(2, checkLimit):
        if isPrime[i]:
            for factor in xrange(2, limit + 1):
                j = i * factor
                if (j > limit): break
                isPrime[j] = False
 
    primes = []
    for i in xrange(1, limit + 1):
        if isPrime[i]:
            primes.append(i)
    return primes

t = input()
inputs = []
for x in xrange(t):
     inputs.append(raw_input().split())

for x in inputs:
    primes = FindPrimes(int(x[1])) - FindPrimes(int(x[0])-1)
    for y in primes:
        i
    print ""        