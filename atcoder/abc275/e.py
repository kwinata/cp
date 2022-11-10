def mod_inverse(A, M):
    return power(A, M - 2, M)
 
def power(x, y, M):
    if (y == 0):
        return 1
    p = power(x, y // 2, M) % M
    p = (p * p) % M
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % M)
 
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

n, m, k = map(int, input())

def div(a, b):
    if gcd(a, b) != 0:
        a /= gcd(a, b)
        b /= gcd(a, b)
    return a * mod_inverse(b)

before_m = n-m