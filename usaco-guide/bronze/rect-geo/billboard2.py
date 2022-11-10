f = open("billboard.in", 'r')
board = list(f.read().split('\n'))
f.close()

def main(board):
    lawnmower = list(map(int, board[0].split()))
    grass = list(map(int, board[1].split()))

    def covered(x, y, rect):
        x1, y1, x2, y2 = rect
        return x1 <= x and x <= x2 and y1 <= y and y <= y2

    covered_count = 0
    for x in (lawnmower[0], lawnmower[2]):
        for y in (lawnmower[1], lawnmower[3]):
            if covered(x, y, grass): # grass will be expanded here to be 4 variables
                covered_count += 1

    def area(rect):
        x1, y1, x2, y2 = rect
        return (x2-x1) * (y2-y1)
    
    if covered_count <= 1:
        return area(lawnmower)

    def find_overlap_area(rect1, rect2):
    # left bottom right top
        l1, b1, r1, t1 = rect1
        l2, b2, r2, t2 = rect2

        # x overlaps = rightmost of left border, leftmost of right border
        x_overlap = max(
            0,  # don't need to take negative value
            min(r1, r2) - max(l1, l2)
        )

        # similarly
        y_overlap = max(
            0,  # don't need to take negative value
            min(t1, t2) - max(b1, b2)
        )

        return x_overlap * y_overlap

    return area(lawnmower) - find_overlap_area(lawnmower, grass)


answer = main(board)
fw = open("billboard.out", "w")
fw.write(str(answer))
