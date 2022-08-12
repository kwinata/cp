n = int(input())

# can change this initial value to space.
# I'm using underscore so it's clearer at the output
grid = [['_']*(2*n+1) for _ in range(2*n+1)]

for i in range(n+1):
	for j in range(n+1):
		value = i+j-n
		if value < 0:
			continue
		grid[i][j] = f'{value}'
		grid[2*n-i][j] = f'{value}'
		grid[i][2*n-j] = f'{value}'
		grid[2*n-i][2*n-j] = f'{value}'

# for i in range(n):
# 	arr = ["_"] * (n+1)
# 	arr[i] = "*"
# 	arr[n-i] = "*"
# 	print(i, n-i, ' '.join(arr))

for row in grid:
	print(' '.join(row))