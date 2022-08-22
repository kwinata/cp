import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

_ = input()
cards = list(map(int, input().split()))

from collections import defaultdict
card_indices = defaultdict(list)
for i, card in enumerate(cards, start=1):
	card_indices[card].append(i)
output = []
for card, indices in card_indices.items():
	if len(indices) % 2:
		print(-1)
		exit()
	for i in range(0, len(indices), 2):
		output.append(f'{indices[i]} {indices[i+1]}')
print('\n'.join(output))