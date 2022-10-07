A, B = map(int, input().split())
postal_code = input()
if len(postal_code) != A+B+1:
    print('No')
    exit()
for i in range(A):
    if postal_code[i] == '-':
        print('No')
        exit()
if postal_code[A] != '-':
    print('No')
    exit()
for i in range(A+1, A+B+1):
    if postal_code[i] == '-':
        print('No')
        exit()
print('Yes')
