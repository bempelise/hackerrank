"""
HackerRank - Project Euler 003

https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N
"""

import math


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def is_perfect_square(number):
    """ Returns true of the given number is a perfect square """
    sqrt = math.sqrt(number)
    return not sqrt - math.floor(sqrt) > 0.0


def g(x, number):
    """ Polynomial """
    return x*x + 1 % number

def get_factor(number):
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = g(x, number)
        y = g(x, number)
        d = gcd(abs(x - y), number)

    if d == number:
        return None
    else:
        return d

def largest_prime_factor(number):
    if number in [1, 0]:
        return None

    # Rho's algorithm does not work with squares
    while is_perfect_square(number):
        number = number / int(math.sqrt(number))

        max_factor = None
    sqrt = math.sqrt(number)
    for i in range(int(sqrt)):
        factor = get_factor(number)
        if max_factor is None or factor > max_factor:
            max_factor = factor
    return max_factor


def print_factors(number):
    sqrt = math.sqrt(number)
    for i in range(int(sqrt)):
        print("{}: {}".format(i, get_factor(number)))

def get_primes(limit):
    primes = []
    current = list(range(2, limit + 1))
    while current:
        next_prime = current[0]
        primes.append(next_prime)
        current[:] = [num for num in current if num % next_prime != 0]
    return primes


def largest_prime_factor_old(number):
    primes = get_primes(number)
    for num in reversed(primes):
        if number % num == 0:
            return num


def main():
    """ main """
    number = 13195
    number = 10416
    number = 4
    # number = 217
    print_factors(number)
    while (largest_prime_factor(number) == largest_prime_factor_old(number)):
        number += 1
    print(number)
    print(largest_prime_factor(number))
    print(largest_prime_factor_old(number))


if __name__ == "__main__":
    main()
