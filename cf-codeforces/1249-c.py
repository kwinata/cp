import sys


def extract_factors(number, base):
    current_power = 1
    powers = []
    while current_power <= number:
        powers.append(current_power)
        current_power *= base

    factors = []
    for power in reversed(powers):
        factor = 0
        while number >= power:
            number -= power
            factor += 1
        factors.append(factor)
    return reversed(factors)


def sum_factors(factors, base):
    multiplier = 1
    total = 0
    for factor in factors:
        total += factor * multiplier
        multiplier *= base
    return total


def biggest_smaller_power(number, base):
    factors = [i for i in extract_factors(number, base)]
    good_limit = 1
    good_factors = []

    carry = 0
    for factor in factors:
        factor += carry
        carry = 0
        if factor > good_limit:
            carry = 1
            good_factors = [0] * (len(good_factors)+1)
        else:
            good_factors.append(factor)
    if carry:
        good_factors.append(carry)
    return sum_factors(good_factors, base)


def test():
    assert 1 == biggest_smaller_power(1, 3)
    assert 3 == biggest_smaller_power(2, 3)
    assert 9 == biggest_smaller_power(6, 3)
    assert 13 == biggest_smaller_power(13, 3)
    assert 27 == biggest_smaller_power(14, 3)
    assert 6561 == biggest_smaller_power(3620, 3)
    assert 19683 == biggest_smaller_power(10000, 3)


if __name__ == "__main__":
    n = int(input())
    for __ in range(n):
        m = int(input())
        print(biggest_smaller_power(m, 3))
