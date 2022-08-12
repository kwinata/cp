s = input()
from collections import Counter
for k, v in Counter(s).items():
	if v == 1:
		print(k)
		exit(0)

print(-1)