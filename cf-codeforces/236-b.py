from collections import defaultdict
import math

problem_size = 1000+1
# precalculate factorisations until 100
primes = [dict() for _ in range(problem_size)]
for i in range(2, problem_size):
	if len(primes[i]) == 0:  # is prime
		p = i
		primes[p][p] = 1 # prime p is divisble by p
		for j in range(p*2, problem_size, p):
			divisible_by = p
			power = 1
			while j % (divisible_by*p) == 0:
				power += 1
				divisible_by *= p
			primes[j][p] = power
	print(i, primes[i])



# actual problem parsing
a, b, c = map(int, input().split())
result = 0
from tqdm import tqdm
for i in tqdm(range(1, a+1)):
	for j in range(1, b+1):
		for k in range(1, c+1):
			# collect all the power herec
			sum_of_primes_power = defaultdict(int)

			for prime, power in primes[i].items():
				sum_of_primes_power[prime] += power
			for prime, power in primes[j].items():
				sum_of_primes_power[prime] += power
			for prime, power in primes[k].items():
				sum_of_primes_power[prime] += power

			# multiplication 'identity' is 1 instead of 0
			total = 1
			for prime, power in sum_of_primes_power.items():
				total *= power+1
			result += total
			result %= 1073741824
print(result)