def is_single_prime_factor(n):
    max_factor = int(1e6+1)
    factor_found = -1
    for i in range(2, max_factor):
        if n % i == 0:
            while n % i == 0 and n > 1:
                n //= i
            if n != 1:
                return 1  # coprime factors found
            return i
    return n

if __name__ == "__main__":
    n = int(input())
    print(is_single_prime_factor(n))

def test():
    assert is_single_prime_factor(4) == 2
    assert is_single_prime_factor(6) == 1
    assert is_single_prime_factor(971324893193) == 1

