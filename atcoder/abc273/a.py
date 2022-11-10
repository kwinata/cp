n = int(input())
arr = [1]
for i in range(1, n+1):
	arr.append(i * arr[-1])
print(arr[-1])