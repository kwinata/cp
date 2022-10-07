def get_bit_1_locations(n):
	"""
	get_bit_1_locations(11) -> [0, 1, 3]

	Pseudocode:
	bit_locs = []
	initialize counter i = 0
	while n > 0:
		if last bit of current n is set (n % 2 == 1):
			add counter i to bit_locs
		divide n by 2 (or bit shift left by 1)
		increase counter
	return bit_locs

	"""
	pass

def generate_powerset(s):
	"""
	generate_powerset([3, 4, 5]) -> [[], [3], [4], [5], [3, 4], [3, 5], [4, 5], [3, 4, 5]]
	
	Pseudocode:
	# initialize with empty powerset
	powerset = [[]]
	for each element:
		create a temporary copy of powersets (temp = powerset)
		for each set in powerset:
			add (set + [element]) into temp
		powerset = temp
	return powerset
	"""
	pass

def calculate_number(bits_set):
	"""
	calculate_number([0, 1, 3]) -> 11

	Pseudocode:
	initialize v = 0
	for each power:
		add 2**power into v
	return v
	"""
	pass

def generate_values(powerset_bits):
	"""
	generate_values([[], [0], [2], [0, 2]]) -> 0, 1, 4, 5
	
	Pseudocode:
	initialize values = []
	for each set_bits in powerset_bits:
		add calculate_number(set_bits) into values
	return values
	"""
	pass


def test():
	assert get_bit_1_locations(11) == [0, 1, 3]
	assert generate_powerset([3, 4, 5]) == [[], [3], [4], [5], [3, 4], [3, 5], [4, 5], [3, 4, 5]]
	assert calculate_number([0, 1, 3]) == 11
	assert generate_values([[], [0], [2], [0, 2]]) == [0, 1, 4, 5]

def main():
	n = int(input())
	bits_set = get_bit_1_locations(n)
	powerset_bits = generate_powerset(bits_set)
	generated_values = generate_values(powerset_bits)
	generated_values.sort()
	print('\n'.join(map(str, generated_values)))


test()
main()
