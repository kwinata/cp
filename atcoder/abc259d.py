
n = int(input())
sx, sy, tx, ty = map(int, input().split())

circles = []
for _ in range(n):
	x, y, r = map(int, input().split())
	circles.append((x, y, r))

from collections import defaultdict

connect = defaultdict(set)
for i in range(len(circles)):
	for j in range(i + 1, len(circles)):
		x1, y1, r1 = circles[i]
		x2, y2, r2 = circles[j]
		dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
		total_radius = (r1 + r2) ** 2
		if dist == total_radius:
			connect[i].add(j)
			connect[j].add(i)
			continue
		if dist > total_radius:
			continue

		# else smaller

		dist_plus_r1 = dist + r1 ** 2
		dist_plus_r2 = dist + r2 ** 2
		if dist_plus_r1 < r2:  # r1 inside r2
			continue
		if dist_plus_r2 < r1:  # r2 inside r1
			continue
		connect[i].add(j)
		connect[j].add(i)



def is_in_circle(x, y, xc, yc, r):
	dist = (x - xc) ** 2 + (y - yc) ** 2
	return r ** 2 == dist


start_circle = None
end_circle = None
for i, c in enumerate(circles):
	if is_in_circle(sx, sy, *c):
		start_circle = i
		break

for i, c in enumerate(circles):
	if is_in_circle(tx, ty, *c):
		end_circle = i
		break

if start_circle is None or end_circle is None:
	print("No")
	exit()
if start_circle == end_circle:
	print("Yes")
	exit()
visited = set()
queue = {start_circle}

while queue:
	cur = queue.pop()
	if cur in visited:
		continue
	nbrs = connect[cur]
	for c in nbrs:
		if c == end_circle:
			print("Yes")
			exit()
		if c not in visited:
			queue.add(c)
	visited.add(cur)

print("No")