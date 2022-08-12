def minimum_action(number_of_tabs, pos, left, right):
    if left > 1 and right < number_of_tabs:  # need to close both sides
        return min(abs(pos-left), abs(pos-right)) + (right-left) + 2
    if left > 1:
        return abs(pos-left) + 1
    if right < number_of_tabs:
        return abs(pos-right) + 1
    return 0


def test():
    assert minimum_action(6, 3, 2, 4) == 5
    assert minimum_action(6, 3, 1, 3) == 1
    assert minimum_action(5, 2, 1, 5) == 0


if __name__=="__main__":
    n, pos, l, r = [int(i) for i in input().split()]
    print(minimum_action(n, pos, l, r))
