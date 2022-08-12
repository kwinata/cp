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


def box(qs):
    possible = set()
    max_added = 0
    result = []
    for q in qs:
        if q > max_added:
            possible |= set(range(max_added + 1, q))
            max_added = q
            result.append(q)
        elif not possible:
            return [-1]
        else:
            result.append(possible.pop())
    return result


for __ in range(t):
    n = int(inp.input())
    qs = inp.input_int_list()
    print(" ".join(map(str, box(qs))))

