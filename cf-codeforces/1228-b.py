class CellType:
    FILLED = 1
    EMPTY = 2
    UNKNOWN = 3


h, w = map(int, input().split())
rs = list(map(int, input().split()))
cs = list(map(int, input().split()))


def fill_the_grid(h, w, rs, cs):
    grid = []
    for i in range(h):
        grid.append([CellType.UNKNOWN] * w)
    for i in range(h):
        r_i = rs[i]
        for j in range(r_i):
            grid[i][j] = CellType.FILLED
        if r_i < w:
            grid[i][r_i] = CellType.EMPTY
    for j in range(w):
        c_i = cs[j]
        for i in range(c_i):
            if grid[i][j] == CellType.EMPTY:
                return 0
            grid[i][j] = CellType.FILLED
        if c_i < h:
            if grid[c_i][j] == CellType.FILLED:
                return 0
            grid[c_i][j] = CellType.EMPTY

    total = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == CellType.UNKNOWN:
                total += 1

    return 2**total % 1000000007


print(fill_the_grid(h, w, rs, cs))
