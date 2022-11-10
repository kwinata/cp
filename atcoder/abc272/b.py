n, m = map(int, input().split())
from collections import defaultdict
parties_attended = defaultdict(set)
for party_idx in range(m):
	arr = list(map(int, input().split()))[1:]
	for attender in arr:
		parties_attended[attender-1].add(party_idx)

for i in range(n):
	for j in range(i+1, n):
		if len(parties_attended[i].intersection(parties_attended[j])) == 0:
			print("No")
			exit()
print("Yes")