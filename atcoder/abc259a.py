n, m, x, t, d = map(int, input().split())

if m >= x:
	print(t)
	exit()
diff = x-m
print(t - d*(diff))
exit()

