n, m = map(int, input().split())
sorted_arr = list(map(int, input().split()))
sorted_arr.sort()
min_dist = 1e9
print(sorted_arr)
for i in range(m-(n-1)):
	print(i, i+(n-1), sorted_arr[i:i+(n)])
	min_dist = min(
		min_dist,
		sorted_arr[i+(n-1)]-sorted_arr[i]
	)
print(min_dist)