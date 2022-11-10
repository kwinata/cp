n, m = map(int, input().split())
from collections import defaultdict
adj = [set() for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a].add(b)
	adj[b].add(a)
for i in range(1, n+1):
	print(len(adj[i]), ' '.join(map(str, sorted(adj[i]))))