import copy


def point_inside(x, y, rect):
    return rect['x1'] <= x <= rect['x2'] and rect['y1'] <= y <= rect['y2']


def white_in_one_black(w, a):
    return point_inside(w['x1'], w['y1'], a) and \
           point_inside(w['x1'], w['y2'], a) and \
           point_inside(w['x2'], w['y1'], a) and \
           point_inside(w['x2'], w['y2'], a)


def white_in_two_black(w, a, b):
    def point_in_one_rect(x, y, a, b):
        return point_inside(x, y, a) or point_inside(x, y, b)
    return point_in_one_rect(w['x1'], w['y1'], a, b) and \
           point_in_one_rect(w['x1'], w['y2'], a, b) and \
           point_in_one_rect(w['x2'], w['y1'], a, b) and \
           point_in_one_rect(w['x2'], w['y2'], a, b)


def black_is_continous(a, b):
    def any_one_point_inside(a, b):
        return point_inside(a['x1'], a['y1'], b) or \
               point_inside(a['x1'], a['y2'], b) or \
               point_inside(a['x2'], a['y1'], b) or \
               point_inside(a['x2'], a['y2'], b)
    return any_one_point_inside(a, b) or any_one_point_inside(b, a)


wx1, wy1, wx2, wy2 = map(int, input().split())
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
w = {'x1': wx1, 'x2': wx2, 'y1': wy1, 'y2': wy2}
a = {'x1': ax1, 'x2': ax2, 'y1': ay1, 'y2': ay2}
b = {'x1': bx1, 'x2': bx2, 'y1': by1, 'y2': by2}


def main(w, a, b):
    if white_in_one_black(w, a) or white_in_one_black(w, b):
        return True
    if not white_in_two_black(w, a, b):
        return False
    return black_is_continous(a, b)


res = main(w, a, b)
print("NO" if res else "YES")
