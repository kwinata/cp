n = int(input())
nums = list(map(int, input().split()))
from collections import Counter
c = Counter(nums)
num_0 = c[0]
num_5 = c[5]

def solve(num_0, num_5):
	if num_0 == 0:
		return "-1"
	if num_5 < 9:
		return "0"
	k = num_5 // 9  # to round down the 5's to multiple of 9
	str_fives = ["5"] * k * 9
	str_zeros = ["0"] * num_0
	return "".join(str_fives + str_zeros)

print(solve(num_0, num_5))