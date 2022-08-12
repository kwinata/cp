"""
the first action allows it to move from (𝑥𝑐, 𝑦𝑐) to (𝑥𝑐−1, 𝑦𝑐);
the second action allows it to move from (𝑥𝑐, 𝑦𝑐) to (𝑥𝑐, 𝑦𝑐+1);
the third action allows it to move from (𝑥𝑐, 𝑦𝑐) to (𝑥𝑐+1, 𝑦𝑐);
the fourth action allows it to move from (𝑥𝑐, 𝑦𝑐) to (𝑥𝑐, 𝑦𝑐−1).

4
2
-1 -2 0 0 0 0
-1 -2 0 0 0 0
3
1 5 1 1 1 1
2 5 0 1 0 1
3 5 1 0 0 0
2
1337 1337 0 1 1 1

1336 1337 1 1 0 1
1
3 5 1 1 1 1

1 -1 -2
1 2 5
0
1 -100000 -100000
"""
from typing import Optional, Tuple


class Robot:
    x: int
    y: int
    left: bool
    top: bool
    right: bool
    down: bool


MAX_VAL = 100000


class Scope:
    def __init__(self):
        self.x_range_min = -MAX_VAL
        self.x_range_max = MAX_VAL
        self.y_range_min = -MAX_VAL
        self.y_range_max = MAX_VAL

    def reduce_scope(self, robot: Robot) -> None:
        if not robot.left:
            self.x_range_min = max(self.x_range_min, robot.x)
        if not robot.right:
            self.x_range_max = min(self.x_range_max, robot.x)
        if not robot.top:
            self.y_range_max = min(self.y_range_max, robot.y)
        if not robot.down:
            self.y_range_min = max(self.y_range_min, robot.y)

    def get_a_solution(self) -> Optional[Tuple[int, int]]:
        if self.x_range_max >= self.x_range_min and self.y_range_max >= self.y_range_min:
            return self.x_range_max, self.y_range_max
        return None


t = int(input())

for i in range(t):
    n = int(input())
    scope = Scope()
    for r_n in range(n):
        values = [int(i) for i in input().split()]
        r = Robot()
        r.x, r.y, r.left, r.top, r.right, r.down = values
        scope.reduce_scope(r)
    sol = scope.get_a_solution()
    if sol is None:
        print(0)
    else:
        print(1, *sol)
