x, k = map(int, input().split())
for i in range(0, k):
	digit = x % 10
	if digit >= 5:
		x += 10-digit
	x //= 10
if x > 0:
	print(x, end="0"*k)
else:
	print(0, end="")
print()
