import sys
			
lines = sys.stdin.readlines()
cleaned_lines = []
prev_line_is_amplifying = True
for line in lines:
	lstripped = line.lstrip()
	is_amplifying = (lstripped and lstripped[0] == '#')
	if is_amplifying:
		if prev_line_is_amplifying == False:
			cleaned_lines.append('\n' + line)
		else:
			cleaned_lines.append(line)
		prev_line_is_amplifying = True
	else:
		cleaned_lines.append(''.join(
			[c for c in line if c not in (' ', '\n')]
		))
		prev_line_is_amplifying = False

# add \n for last line if not amplifying
if not prev_line_is_amplifying:
	cleaned_lines[-1] += '\n'
out = ''.join(cleaned_lines)
print(''.join(cleaned_lines), end='')  # don't print extra \n
