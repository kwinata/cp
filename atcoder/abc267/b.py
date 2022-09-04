s = input()

groups = [{7}, {4}, {2, 8}, {5, 1}, {3, 9}, {6}, {10}]
for i, c in enumerate(s):
  if i == 0 and c == '1':
    print("No")
    exit()
  if c == '1':
    continue
  for group in groups:
    if (i+1) in group:
      group.remove(i+1)

state = 0
for group in groups:
  n = len(group)
  if state == 0 and n > 0:
    state = 1
    continue
  if state == 1 and n == 0:
    state = 2
    continue
  if state == 2 and n > 0:
    state = 3
    print("Yes")
    exit()
print("No")
