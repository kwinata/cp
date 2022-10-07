a, b, d = map(int, input().split())

import math
r = math.radians(d)

x = a*math.cos(r) - b*math.sin(r)
y = a*math.sin(r) + b*math.cos(r)
print(x, y)
print(len(set(map(int, input().split()))))

s = input()
t = input()[:len(s)]
print("Yes" if s == t else "No")