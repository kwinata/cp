"""
input:
6
7
2323216
1615124
1
3
4
2
13
24
2
12
34
3
536
345
2
46
54

output:
YES
YES
YES
NO
YES
NO
"""
from typing import Tuple, List, Dict


class PipeType:
    STRAIGHT = 1
    BENT = 2


class Board:
    def __init__(self, num_of_cols: int, pipes: Tuple[List[int], List[int]]):
        self.num_of_cols = num_of_cols
        self.verticals = {'top': Board.init_false_array(num_of_cols+1), 'bottom': Board.init_false_array(num_of_cols+1)}
        self.pipes = {'top': list(map(Board.transform_pipe_type, pipes[0])),
                      'bottom': list(map(Board.transform_pipe_type, pipes[1]))}
        self.verticals['top'][0] = True

    @staticmethod
    def transform_pipe_type(original_pipe_type: int):
        if original_pipe_type in [1, 2]:
            return PipeType.STRAIGHT
        else:
            return PipeType.BENT

    def __connect(self, col_num: int):
        for row in ['top', 'bottom']:
            if self.pipes[row][col_num] == PipeType.STRAIGHT:
                self.verticals[row][col_num+1] |= self.verticals[row][col_num]

        if self.pipes['top'][col_num] == PipeType.BENT and self.pipes['bottom'][col_num] == PipeType.BENT:
            self.verticals['top'][col_num + 1] |= self.verticals['bottom'][col_num]
            self.verticals['bottom'][col_num + 1] |= self.verticals['top'][col_num]

    @staticmethod
    def init_false_array(length: int):
        return [False] * length

    def __connect_all(self):
        for i in range(self.num_of_cols):
            self.__connect(i)

    def connected(self) -> bool:
        self.__connect_all()
        return self.verticals['bottom'][self.num_of_cols]


def test():
    assert Board(7, ([2, 3, 2, 3, 2, 1, 6],
                      [1, 6, 1, 5, 1, 2, 4])).connected()
    assert Board(1, ([3], [4])).connected()
    assert Board(2, ([1, 3], [2, 4])).connected()
    assert not Board(2, ([1, 2], [3, 4])).connected()
    assert Board(3, ([5, 3, 6], [3, 4, 5])).connected()
    assert not Board(2, ([4, 6], [5, 4])).connected()


if __name__ == "__main__":
    q = int(input())
    for __ in range(q):
        n = int(input())
        top = [int(c) for c in input()]
        bottom = [int(c) for c in input()]
        if Board(n, (top, bottom)).connected():
            print("YES")
        else:
            print("NO")
