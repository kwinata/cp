billboard1 = list(map(int, input().split()))
billboard2 = list(map(int, input().split()))
truck = list(map(int, input().split()))

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
