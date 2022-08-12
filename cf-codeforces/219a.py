k = int(input())
letters = input()

from collections import defaultdict
letter_count = defaultdict(int)

for c in letters:
    if c in letter_count.keys():
        letter_count[c] += 1
    else:
        letter_count[c] = 1
print(letter_count)

counts = defaultdict(int)
unit = ''
for key, value in letter_count.items():
    if value % k != 0:
        print(-1)
        break
    else:
        counts[key] = int(value / k)
for keys, values in counts.items():
    unit += keys * values
print(counts)
print(unit)