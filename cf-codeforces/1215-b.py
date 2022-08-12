__ = input()
arr = map(int, input().split())
pos = [0]
neg = [0]
for a in arr:
    if a > 0:
        pos.append(pos[-1])
        neg.append(neg[-1])
        pos[-1] += 1
    else:
        neg.append(pos[-1])
        pos.append(neg[-2])  # -2 instead of -1 because last is added in previous statement
        neg[-1] += 1
print(sum(neg), sum(pos))
