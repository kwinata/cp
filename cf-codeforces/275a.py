grid = [list(map(int, input().split())) for _ in range(3)]
# print(grid)

grid_normalized = [[value % 2 for value in row] for row in grid]

def print_nice(g):
	print('\n'.join([''.join(map(str, row)) for row in g]))

# print_nice(grid_normalized)

offsets = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]

state = [[1 for _ in range(3)] for _ in range(3)]

def in_the_box(x, y):
	return x < 3 and x >= 0 and y < 3 and y >= 0 

for i in range(3):
	for j in range(3):
		toggled = grid_normalized[i][j]
		if not toggled:
			continue
		for di, dj in offsets:
			light_i = i + di
			light_j = j + dj
			if not in_the_box(light_i, light_j):
				continue
			state[light_i][light_j] ^= 1
print_nice(state)
