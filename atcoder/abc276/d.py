n = int(input())
arr = list(map(int, input().split()))
pow2s = [0] * n
pow3s = [0] * n
residues = []
for i, v in enumerate(arr):
	while v & 1 == 0:
		pow2s[i] += 1
		v >>= 1
	while v % 3 == 0:
		pow3s[i] += 1
		v //= 3
	residues.append(v)
if len(set(residues)) > 1:
	print(-1)
	exit()

minpow2 = min(pow2s)
minpow3 = min(pow3s)
total_action = 0
for pow2 in pow2s:
	total_action += pow2 - minpow2
for pow3 in pow3s:
	total_action += pow3 - minpow3
print(total_action)