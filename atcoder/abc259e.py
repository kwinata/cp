import sys

lines = sys.stdin.readlines()[::-1]

n = int(lines.pop())
numbers = []
from collections import defaultdict
biggest_power = defaultdict(int)
for _ in range(n):
    f_count = int(lines.pop())
    f_dict = {}
    for _ in range(f_count):
        p, e = map(int, lines.pop().split())
        f_dict[p] = e
        biggest_power[p] = max(e, biggest_power[p])
    numbers.append(f_dict)

count_peaks = defaultdict(int)
for num in numbers:
    for p, e in num.items():
        if e == biggest_power[p]:
            count_peaks[p] += 1

dominant = []
for num in numbers:
    def find_dominant():
        for p, e in num.items():
            if count_peaks[p] == 1 and e == biggest_power[p]:
                dominant.append(p)
                return
        dominant.append(0)
    find_dominant()
print(len(set(dominant)))