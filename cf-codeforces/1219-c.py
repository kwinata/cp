#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Periodic integer number

Alice became interested in periods of integer numbers. We say positive 𝑋 integer number is periodic with length 𝐿 if
there exists positive integer number 𝑃 with 𝐿 digits such that 𝑋 can be written as 𝑃𝑃𝑃𝑃…𝑃. For example:

𝑋=123123123
is periodic number with length 𝐿=3 and 𝐿=9

𝑋=42424242
is periodic number with length 𝐿=2,𝐿=4 and 𝐿=8

𝑋=12345
is periodic number with length 𝐿=5

For given positive period length 𝐿
and positive integer number 𝐴, Alice wants to find smallest integer number 𝑋 strictly greater than 𝐴
that is periodic with length L.

Input

First line contains one positive integer number 𝐿 (1≤𝐿≤105)
representing length of the period. Second line contains one positive integer number 𝐴 (1≤𝐴≤10100000).

Output

One positive integer number representing smallest positive number that is periodic with length 𝐿
and is greater than 𝐴.

Examples
Input
3
123456

Output
124124

Input
3
12345

Output
100100

Note

In first example 124124 is the smallest number greater than 123456 that can be written with period L = 3 (P = 124).

In the second example 100100 is the smallest number greater than 12345 with period L = 3 (P=100)
"""
import math
from typing import List, Tuple


def generate_1000s(number_of_period: int, length: int) -> int:
    period = ["1"] + ["0"]*(length - 1)
    period *= number_of_period
    return int("".join(period))


def test_generate_1000s():
    assert generate_1000s(4, 3) == 100100100100
    assert generate_1000s(1, 7) == 1000000


def find_smallest_next_periodic(periods: List[int]) -> Tuple[int, int]:
    initial_periodic_guess = periods[0]
    for period in periods:
        if initial_periodic_guess < period:
            return increment_periodic_value(initial_periodic_guess)
        elif initial_periodic_guess == period:
            continue
        elif initial_periodic_guess > period:
            return initial_periodic_guess, 0
    return increment_periodic_value(initial_periodic_guess)


def increment_periodic_value(value: int) -> Tuple[int, int]:
    if value == 10**(len(str(value)))-1:
        return generate_1000s(1, len(str(value))), 1
    else:
        return value+1, 0


def test_find_smallest_next_periodic():
    assert find_smallest_next_periodic([123, 124]) == (124, 0)
    assert find_smallest_next_periodic([123, 123, 122]) == (123, 0)
    assert find_smallest_next_periodic([12, 12, 12]) == (13, 0)
    assert find_smallest_next_periodic([999, 999, 999]) == (100, 1)


def smallest_periodic_after(a: int, length: int) -> int:
    if len(str(a)) % length == 0:
        a_str = str(a)
        cycles = len(a_str)//length
        periods = [int(a_str[i*length:(i+1)*length]) for i in range(cycles)]
        periodic_value, cycle_increment = find_smallest_next_periodic(periods)
        return int("".join([str(periodic_value)]*(cycles+cycle_increment)))
    else:
        return generate_1000s(math.ceil(len(str(a)) / length), length)


def test_smallest_periodic_after():
    assert smallest_periodic_after(123456, 3) == 124124
    assert smallest_periodic_after(12345, 3) == 100100
    assert smallest_periodic_after(999999999, 3) == 100100100100


if __name__ == "__main__":
    l = int(input())
    a = int(input())
    print(smallest_periodic_after(a, l))
