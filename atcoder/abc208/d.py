s = input()
def sol(s):
  if s[0] != s[-1]:
    return 1
  for i in range(len(s)-1):
    if s[0] != s[i] and s[0] != s[i+1]:
      return 2
  return -1
print(sol(s))
