"""

a1 a2 a3 a4 a5



5 1 2 3 4 -> 1 2 3 4 5
"""

n = int(input())

output = [n]
for i in range(1, n):
	output.append(i)
print(" ".join(output))

n = int(input())
arr = list(map(lambda x: x, range(1, n+1)))


def swap(x):
	print(f"{'  ' * (n-x) + '-> '}call swap({x})")
	arr[x-1], arr[x-2] = arr[x-2], arr[x-1]


def f(x):
	if x == 1:
		print(f"{'  ' * (n-x)}hit base condition x==1")
		return
	
	print(f"{'  ' * (n-x)}f({x}): before swap: {arr}")
	swap(x)
	print(f"{'  ' * (n-x)}f({x}): after swap: {arr}")


	print(f"{'  ' * (n-x)}f({x}): before recurse: {arr}")
	f(x-1)
	print(f"{'  ' * (n-x)}f({x}): after recurse: {arr}")



f(n)