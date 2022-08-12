n = int(input())

arr = []
for i in range(n):
    row = []
    j_range = range(1, n+1)
    if i & 1:
        j_range = reversed(j_range)
    for j in j_range:
        row.append(i*n + j)
    arr.append(row)

for i in range(n):
    for j in range(n):
        print(arr[j][i], end=" ")
    print()
