from sys import stdin
 
def exchange(n, _cache = {0: 0}):
 	if not _cache.has_key(n):
        v = exchange(n//2) + exchange(n//3) + exchange(n//4)
        _cache[n] = max(n, v)
    return _cache[n]
 
def main():
 	for n in map(int, stdin):
        print exchange(n)
 
if __name__ == '__main__':
    main()