x, y, z = map(int, input().split())

sign = lambda p: p / abs(p)

def calc(x, y, z):
	# y and x is different dir
	if sign(y) != sign(x):
		return abs(x)

	# x is closer to y anyway
	if abs(x) < abs(y):
		return abs(x)

	# need to break wall, but y is closer than z
	if sign(y) == sign(z) and abs(y) < abs(z):
		return -1

	# go to the hammer, then go to x without any wall
	return abs(z) + abs(x-z)

print(calc(x, y, z))