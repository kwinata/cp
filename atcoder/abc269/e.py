n = int(input())


def ask(a, b, c, d):
	print(f"? {a} {b} {c} {d}")
	resp = int(input())
	return resp

# bfs l. r
l = 1
r = n
in_range = n
while l < r:
	mid = (l+r)//2
	t = ask(l, mid, 1, n)
	if t < (mid-l)+1:
		r = mid
	else:
		l = mid+1

x = l

# bfs heihgt
l = 1
r = n
in_range = n
while l < r:
	mid = (l+r)//2
	t = ask(1, n, l, mid)
	if t < (mid-l)+1:
		r = mid
	else:
		l = mid+1

y = l

print(f"! {x} {y}")