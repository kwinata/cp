n = int(input())
cities = []
for _ in range(n):
	cities.append(list(map(int, input().split())))

def dist(cities, i, j):
	return (
		abs(cities[i][0] - cities[j][0]) +
		abs(cities[i][1] - cities[j][1]) +
		max(0, cities[i][2] - cities[j][2])
	)

cache = {}
def dp(i, s):
	print("calling dp", i, bin(s))
	# if no city is visited
	if s == 0:
		return 0

	# if the only visited city is the current one
	if s == 1 << i:
		return 0

	if (i, s) in cache:
		return cache[(i, s)]

	min_val = 1e9
	s_copy = s
	for j in range(n):
		# if the j-th bit is set
		jth_bit_set = s_copy & 1
		s_copy >>= 1
		if j == i:
			continue

		print("checking prev", j, bool(jth_bit_set))

		if jth_bit_set and s & (1<<j):
			s_min_j = (s - (1<<j)) if (s & (1<<j)) else s
			print("downstream dp", j, bin(s_min_j))
			min_val = min(min_val, dp(j, s_min_j) + dist(cities, i, j))

	cache[(i, s)] = min_val
	return min_val

print(dp(0, (1<<n) - 1))