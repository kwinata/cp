import math

t = int(input())
for __ in range(t):
    a, b = map(int, input().split())
    d = abs(b-a)
    print(d//5 + math.ceil(d % 5 / 2))
