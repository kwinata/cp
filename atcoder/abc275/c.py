arr = [input() for _ in range(9)]
pawns = []
for i in range(9):
	for j in range(9):
		if arr[i][j] == '#':
			pawns.append((i, j))
pawns_set = set(pawns)

squares = set()
for i in range(len(pawns)):
	for j in range(i+1, len(pawns)):
		points = [pawns[i], pawns[j]]
		dx = pawns[i][0]-pawns[j][0]
		dy = pawns[i][1]-pawns[j][1]

		sq1p1 = (pawns[i][0]+dy, pawns[i][1]-dx)
		sq1p2 = (pawns[j][0]+dy, pawns[j][1]-dx)

		sq2p1 = (pawns[i][0]-dy, pawns[i][1]+dx)
		sq2p2 = (pawns[j][0]-dy, pawns[j][1]+dx)

		if sq1p1 in pawns_set and sq1p2 in pawns_set:
			squares.add(tuple(sorted((pawns[i], pawns[j], sq1p1, sq1p2))))
		if sq2p1 in pawns_set and sq2p2 in pawns_set:
			squares.add(tuple(sorted((pawns[i], pawns[j], sq2p1, sq2p2))))
print(len(squares))