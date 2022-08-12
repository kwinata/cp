s = input()
t = input()

def split_to_token(s):
	heads = [0]
	for i in range(1, len(s)):
		if s[i-1] != s[i]:
			heads.append(i)
	heads.append(len(s))
	tokens = []
	for i in range(len(heads)-1):
		tokens.append(s[heads[i]:heads[i+1]])
	return tokens
s_tokens = split_to_token(s)
t_tokens = split_to_token(t)

if len(s_tokens) != len(t_tokens):
	print("No")
	exit()

for i in range(len(s_tokens)):
	s_token = s_tokens[i]
	t_token = t_tokens[i]
	if s_token[0] != t_token[0]:
		print("No")
		exit()
	if len(s_token) == len(t_token):
		continue
	if len(s_token) > len(t_token):
		print("No")
		exit()
	if len(s_token) == 1:
		print("No")
		exit()
print("Yes")
