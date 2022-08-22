x, y, n = map(int, input().split())
is_3_cheaper = x*3 >= y
if is_3_cheaper:
	print(y * (n//3) + x * (n % 3))
else:
	print(x*n)
