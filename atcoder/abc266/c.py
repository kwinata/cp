coords = []
for _ in range(4):
	x, y = map(int, input().split())
	coords.append((x, y))

res = set()

for i in range(4):
	p, q, r = coords[i], coords[(i+1) % 4], coords[(i+2) % 4]

	dx1 = q[0] - p[0]
	dy1 = q[1] - p[1]
	dx2 = r[0] - q[0]
	dy2 = r[1] - q[1]

	if (dx1*dy2 - dy1*dx2) <= 0:
		print("No")
		exit(0)

print("Yes")