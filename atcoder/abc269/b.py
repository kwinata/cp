arr = [input() for _ in range(10)]
min_a = 10
min_c = 10
max_b = -1
max_d = -1
for i in range(10):
	for j in range(10):
		if arr[i][j] == '#':
			min_a = min(min_a, i)
			min_c = min(min_c, j)
			max_b = max(max_b, i)
			max_d = max(max_d, j)
print(min_a+1, max_b+1)
print(min_c+1, max_d+1)