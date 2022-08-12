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


def make_tidy(n, s: str):
    if s == '()':
        return []
    if s == ')(':
        return [[0, 1]]
    stack_ = []
    for i, c in enumerate(s):
        if stack_ and c == ')' and stack_[-1][0] == '(':
            stack_.pop()
        else:
            stack_.append([c, i])
    if stack_:
        i = 0
        while stack_[i][0] == ')':
            i += 1
        return [
            [stack_[i][1], n-1],  # take out the clean element and put it at the back
            [(stack_[i-1][1]+n-stack_[i][1]), n-1],  # fix the accidental reversed
            [0, (stack_[i-1][1]+n-stack_[i][1])]  # reverse the messy part, done
        ]
    return []


def reverse(s, l, r):
    if l >= len(s) or r >= len(s):
        raise ValueError()
    return s[:l] + s[l:r+1][::-1] + s[r+1:]


def test_make_tidy():
    n = 10
    s = "))()()()(("
    actions = make_tidy(n, s)
    for action in actions:
        s = reverse(s, *action)
    assert s == "(())()()()"

    n = 2
    s = ")("
    actions = make_tidy(n, s)
    for action in actions:
        s = reverse(s, *action)
    assert s == "()"


def antidote(c):
    return ')' if c == '(' else '('


def count_current_k(s):
    stack_ = []
    k = 0
    start_boundary = 0
    boundaries = []
    for i, c in enumerate(s):
        if stack_ and stack_[-1] == antidote(c):
            stack_.pop()
        else:
            stack_.append(c)
        if not stack_:
            boundaries.append([start_boundary, i])
            start_boundary = i+1
            k += 1
    return k, boundaries


def pop_baloon(s, actions, base):
    if len(s) == 2:
        return s
    cur_k, boundaries = count_current_k(s)
    if cur_k == len(s)//2:
        return s
    for start, end in boundaries:
        if end - start <= 2:
            continue
        else:
            s = s[:start+1] + s[end:] + pop_baloon(s[start+1:end], actions, base+start+1)
            actions.extend([[base+start+1, base+end], [base+start+2, base+end]])
    return s


def test_pop():
    print()
    actions = []
    s = "(()((())))"
    assert pop_baloon(s, actions, 0) == "()()()()()"
    for action in actions:
        s = reverse(s, *action)
        print(action, s)
    assert s == "()()()()()"
    assert pop_baloon("()", [], 0) == "()"


def construct(s, actions, k):
    cur_k = len(s)//2
    diff = cur_k - k
    if diff == 0:
        return
    actions.append([1, diff*2])


def test_count_k():
    assert 4, [[0, 3], [4, 5], [6, 7], [8, 9]] == count_current_k("(())()()()")


if __name__ == "__main__":
    inp = Input()
    t = int(inp.input())

    for __ in range(t):
        n, k = inp.input_int_list()
        s = inp.input()

        # print(s)

        actions = make_tidy(n, s)
        for action in actions:
            s = reverse(s, *action)
        # print(s)

        discard = len(actions)
        pop_baloon(s, actions, 0)
        for action in actions[discard:]:
            s = reverse(s, *action)
        # print(s)

        discard = len(actions)
        construct(s, actions, k)
        for action in actions[discard:]:
            s = reverse(s, *action)
        print(s)

        for action in actions:
            if action[0] == action[1]:
                actions.remove(action)
        print(len(actions))
        for action in actions:
            print(*(map(lambda x: x+1, sorted(action))))
