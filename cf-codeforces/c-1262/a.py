import heapq


class Input:
    def __init__(self):
        from sys import stdin
        lines = stdin.readlines()
        self.lines = list([line.rstrip('\n') for line in reversed(lines) if line != '\n'])

    def input(self):
        return self.lines.pop()

    def input_int_list(self):
        return list(map(int, self.input().split()))

    def __bool__(self):
        return bool(self.lines)


inp = Input()
t = int(inp.input())
for __ in range(t):
    n = int(inp.input())
    min_right = []
    max_left = []
    min_distance = 0
    for i in range(n):
        l, r = inp.input_int_list()
        if min_right:
            min_distance = max(l - min_right[0], min_distance)
        if max_left:
            min_distance = max(-max_left[0] - r, min_distance)
        heapq.heappush(min_right, r)
        heapq.heappush(max_left, -l)
    print(min_distance)
