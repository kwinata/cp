n = int(input())
arr = []
for i in range(60):
	v = n & 1
	if v == 1:
		arr.append(i)
	n >>= 1

from itertools import chain, combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

vals = []

for pows in powerset(arr):
	v = 0
	for power in pows:
		v |= 1 << power
	vals.append(v)
vals.sort()
print('\n'.join(map(str, vals)))