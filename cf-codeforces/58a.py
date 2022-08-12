s = input()

tofind = list("hello")
tofind.reverse()


for c in s:
	if c == tofind[-1]:
		tofind.pop()
		if len(tofind) == 0:  # stop searching
			break

if len(tofind) > 0:
	print("NO")
else:
	print("YES")