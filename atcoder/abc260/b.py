n, x, y, z = map(int, input().split())
a = [
	(score, i+1) 
	for i, score in enumerate(
		map(int, input().split())
	)
]
b = [
	(score, i+1) 
	for i, score in enumerate(
		map(int, input().split())
	)
]

a.sort(key=lambda x: (-x[0], x[1]))
print(a, b)
x_admitted = {student for score, student in a[:x]}
print(x_admitted)
a = a[x:]
b = [(score, student) for score, student in b if student not in x_admitted]
print(a, b)


b.sort(key=lambda x: (-x[0], x[1]))
y_admitted = {student for score, student in b[:y]}
print(y_admitted)
b = b[y:]
a = [(score, student) for score, student in a if student not in y_admitted]

from collections import defaultdict
combinedscore = defaultdict(int)
for score, student in (a+b):
	combinedscore[student] += score
combinedscore = [(score, student) for student, score in combinedscore.items()]
combinedscore.sort(key=lambda x: (-x[0], x[1]))
z_admitted = {student for score, student in combinedscore[:z]}
print(z_admitted)

admitted = [student for student in x_admitted.union(y_admitted).union(z_admitted)]
admitted.sort()
print('\n'.join(map(str, admitted)))