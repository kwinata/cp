import math
N = int(input())
def prime(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True
if prime(N):
    print(1)
    print(N)
else:
    for i in range(1, N+1):
        if N % i == 0:
            print(i)