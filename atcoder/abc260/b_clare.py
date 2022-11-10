# N, X, Y, Z = map(int, input().split())
# maths = list(map(int, input().split()))
# eng = list(map(int, input().split()))
# students = list()
# for i in range(N):
#     students.append((maths[i], eng[i], i))
# math_sort = sorted(students, key=lambda x:(-x[0], x[1])) # this one supposed to be (-x[0], x[2])? tie breaker is student id
# selected = list()
# for i in range(X):
#     selected.append(math_sort[i][2]+1)
# eng_sort = sorted(math_sort[X:], key=lambda x:(-x[0], x[1])) # this one should sort by (-x[1], x[2])?
# for i in range(Y):
#     selected.append(eng_sort[i][2]+1)
# total = eng_sort[Y:]
# total_ = list()
# for item in total:
#     total_.append((item[0] + item[1], item[2]))
# total_sort = sorted(total_, key=lambda x:(-x[0], x[1]))
# for i in range(Z):
#     selected.append(total_sort[i][1]+1)
# selected.sort()
# for i in selected:
#     print(i)

N, X, Y, Z = map(int, input().split())
maths = list(map(int, input().split()))
eng = list(map(int, input().split()))
students = list()
for i in range(N):
    students.append((maths[i], eng[i], i))
math_sort = sorted(students, key=lambda x:(-x[0], x[2])) # this one supposed to be (-x[0], x[2]). tie breaker is student id
selected = list()
for i in range(X):
    selected.append(math_sort[i][2]+1)
eng_sort = sorted(math_sort[X:], key=lambda x:(-x[1], x[2])) # this one should sort by (-x[1], x[2]).
for i in range(Y):
    selected.append(eng_sort[i][2]+1)
total = eng_sort[Y:]
total_ = list()
for item in total:
    total_.append((item[0] + item[1], item[2]))
total_sort = sorted(total_, key=lambda x:(-x[0], x[1]))
for i in range(Z):
    selected.append(total_sort[i][1]+1)
selected.sort()
for i in selected:
    print(i)