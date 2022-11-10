t = int(input())
for _ in range(t):
	w, h = map(int, input().split())
	rect = list(map(int, input().split()))
	wt, ht = map(int, input().split())
	def solve(w, h, rect, wt, ht):
		# attemp top
		def test(gap, othergap, cross, sz, cross_sz):
			if cross < cross_sz:
				return -1
			if gap < sz:
				move = sz-gap
				othergap -= move
				if othergap < 0:
					return -1
				return move
			return 0
		vals = [
			test(rect[0], w-rect[2], h, wt, ht),
			test(w-rect[2], rect[0], h, wt, ht),
			test(rect[1], h-rect[3], w, ht, wt),
			test(h-rect[3], rect[1], w, ht, wt),
		]
		vals = [v for v in vals if v != -1]
		if len(vals) == 0:
			return -1
		return min(vals)
	print(solve(w, h, rect, wt, ht))