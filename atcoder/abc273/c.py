def main():
	n = int(input())
	arr = list(map(int, input().split()))

	s = list(set(arr))
	s.sort()

	from collections import Counter, defaultdict
	c = Counter(arr)
	m = defaultdict(int)
	for i, v in enumerate(s):
		# print(i, v, len(s)-i-1)
		m[len(s)-i-1] = v

	for i in range(n):
		print(c[m[i]])
main()