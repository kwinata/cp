n, x, y = map(int, input().split())

r, b = 1, 0
for i in range(n-1):
	b += r*x
	r += b
	b *= y
print(b)