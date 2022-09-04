e = [3.5]

import math
n = int(input())
for i in range(n-1):
	chances = 6 - math.floor(e[-1])
	avg = (6 + math.ceil(e[-1])) / 2
	e.append(
		(
			(e[-1]*(6-chances)) + (avg*chances)
		) / 6.0
	)
print(e[-1])