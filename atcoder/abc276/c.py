n = int(input())
arr = list(map(int, input().split()))
breakpoint = None
for i in range(n-1, 0, -1):
	if arr[i-1] > arr[i]:
		breakpoint = i-1
		break
def niceprint(arr):
	print(' '.join(map(str, arr)))
if breakpoint is None:
	niceprint(arr)
	exit()
prefix = arr[:breakpoint]
suffix = arr[breakpoint:]

head = suffix[0]
the_rest = set(suffix[1:])
next_smallest = None
for cdt in range(head-1, 0, -1):
	if cdt in the_rest:
		next_smallest = cdt
		break
the_rest.remove(next_smallest)
the_rest.add(head)
suffix = [next_smallest] + list(sorted(the_rest, key=lambda x: -x))

niceprint(prefix + suffix)