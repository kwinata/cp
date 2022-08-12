"""
8
0 1 2 3 4 5 6 7
1 2 1 3 1 2 1 5

x = 1
0, 2, 4, 6 (yes)
1 -> 2

x = 2
1, 5 (yes)
2 -> 4

x = 3
3 (yes)
3 -> 0

x = 4 (no)

x = 5
7 (yes)
5 -> 0
"""

# 1
# x = 2, px = 0

# 10^5
# 1, 2, 3, 4, 5, ..., 10^5

n = int(input())
arr = list(map(int, input().split()))
numbers_to_try = dict()
for i, ai in enumerate(arr):
	if ai in numbers_to_try:
		numbers_to_try[ai].append(i)
	else:
		numbers_to_try[ai] = [i]
print(numbers_to_try)

# for number, indices in numbers_to_try.items():
# 	check_arithmetic(indices)


# > 10^9 TLE




