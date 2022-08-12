n, m = map(int, input().split())
arr = list(map(int, input().split()))

pos = 1
dist = 0

for loc in arr:
	dist += (loc - pos) % n
	pos = loc

print(dist)