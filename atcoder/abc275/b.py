m = 998244353 
def mul_mod(a, b):
	return ((a % m) * (b % m)) % m

a, b, c, d, e, f = map(int, input().split())

print(
	(mul_mod(mul_mod(a, b), c) - mul_mod(mul_mod(d, e), f)) % m
)