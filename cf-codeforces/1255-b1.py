"""
4
5 2 2
1 2 1 2 1
9 3 3
3 3 3 2 2 2 1 1 1
4 10 4
10 8 6 4
16 9 8
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3

2
1
4
5

idea: have a frame of size d, keep track of the size
"""


class Multiset:
    def __init__(self, initial):
        self.d = {}
        for i in initial:
            self.add(i)

    def add(self, i):
        if i in self.d:
            self.d[i] += 1
        else:
            self.d[i] = 1

    def remove(self, i):
        if i not in self.d:
            raise KeyError()
        if self.d[i] == 1:
            del self.d[i]
        else:
            self.d[i] -= 1

    def size(self):
        return len(self.d)


def minimum_show(d, shows) -> int:
    frame = Multiset(shows[:d])
    min_show = frame.size()
    for i in range(0, len(shows)-d):
        frame.remove(shows[i])
        frame.add(shows[i+d])
        min_show = min(min_show, frame.size())
    return min_show


def test_min_show():
    assert minimum_show(2, [1, 2, 1, 2, 1]) == 2
    assert minimum_show(3, [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1
    assert minimum_show(4, [10, 8, 6, 4]) == 4
    assert minimum_show(8, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]) == 5


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        __, __, d = (int(i) for i in input().split())
        shows = [int(i) for i in input().split()]
        print(minimum_show(d, shows))
