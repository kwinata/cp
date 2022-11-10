input()
arr = list(map(int, input().split()))

odd = [i for i in arr if i & 1]
even = [i for i in arr if i & 1 == 0]

if len(odd) < 2 and len(even) < 2:
	print(-1)
	exit()

odd.sort()
even.sort()

max_val = -1
if len(odd) >= 2:
	max_val = max(odd[-1] + odd[-2], max_val)
if len(even) >= 2:
	max_val = max(even[-1] + even[-2], max_val)
print(max_val)