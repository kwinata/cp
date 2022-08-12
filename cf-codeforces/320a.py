s = input()

def solve(s):
	cur = "init"
	for c in s:
		if cur == "init":
			if c == "1":
				cur = "one"
			else:
				return "NO"
		elif cur == "one":
			if c == "1":
				cur = "one"	
			elif c == "4":
				cur = "oneFour"
			else:
				return "NO"
		elif cur == "oneFour":
			if c == "1":
				cur = "one"
			elif c == "4":
				cur = "oneFourFour"
			else:
				return "NO"
		elif cur == "oneFourFour":
			if c == "1":
				cur = "one"
			else:
				return "NO"

	# if no "NO" was returned while going through, then it's success
	return "YES"

print(solve(s))