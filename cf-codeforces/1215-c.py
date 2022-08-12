from collections import defaultdict

n = int(input())
s = input()
t = input()

d = []
for i, c in enumerate(s):
    if c != t[i]:
        d.append([c, i+1])

if len(d) % 2:
    print(-1)
    exit()

locs = defaultdict(list)
for diff in d:
    locs[diff[0]].append(diff[1])

if len(locs['a']) % 2:
    print(len(d)//2+1)
else:
    print(len(d)//2)

while len(locs['a']) >= 2:
    print(locs['a'].pop(), locs['a'].pop())
while len(locs['b']) >= 2:
    print(locs['b'].pop(), locs['b'].pop())
if locs['a']:
    print(locs['a'][0], locs['a'][0])
    print(locs['a'][0], locs['b'][0])