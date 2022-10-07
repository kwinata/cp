n = int(input())
arr = list(map(int, input().split()))

initial_sum = sum(arr)
max_gain = -1

prefix_sum_count_0 = [0]
cur_sum = 0
for i in range(n):
	if arr[i] == 0:
		cur_sum += 1
	prefix_sum_count_0.append(cur_sum)

prefix_sum_count_1 = [0]
cur_sum = 0
for i in range(n):
	if arr[i] == 1:
		cur_sum += 1
	prefix_sum_count_1.append(cur_sum)


def calc_gain(i, j):
	global prefix_sum_count_0, prefix_sum_count_1

	count_0 = prefix_sum_count_0[j+1] - prefix_sum_count_0[i]
	count_1 = prefix_sum_count_1[j+1] - prefix_sum_count_1[i]

	gain = count_0 - count_1
	# print(f"{i} to {j}, count_0: {count_0}, count_1: {count_1}")
	return gain



for i in range(n):  # n
	for j in range(i, n):  # n
		gain = calc_gain(i, j)
		max_gain = max(max_gain, gain)
print(initial_sum + max_gain)