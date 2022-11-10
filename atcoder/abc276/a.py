a = None
s = input()
for i, c in enumerate(s):
	if c == 'a':
		a = i+1
if a is None:
	print(-1)
else:
	print(a)