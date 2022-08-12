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
    x, y = inp.input_int_list()
    if x >= y:
        print("YES")
    else:
        prev_x = x
        while x <= y:
            x //= 2
            x *= 3
            if x >= y:
                print("YES")
                break
            elif x <= prev_x:
                print("NO")
                break
            else:
                prev_x = x
        else:
            print("YES")
