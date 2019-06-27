"""
HackerRank - Project Euler 003

https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N
"""


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def get_factor(number):

    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1

    while factor == 1:
        count = 1
        while count <= cycle_size and factor <= 1:
            x = (x*x + 1) % number
            factor = gcd(x - x_fixed, number)
            count += 1
        cycle_size *= 2
        x_fixed = x
    return factor


def largest_prime_factor(number):
    if number in [1, 0]:
        return None

    while number % 2 == 0:
        factor = 2
        number /= 2

    while int(number) > 1:
        factor = get_factor(number)
        while number % factor == 0:
            number /= factor
    return int(factor)


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
    number = 1
    number = 25
    while (largest_prime_factor(number) == largest_prime_factor_old(number)):
        number += 1
    print(number)
    print(largest_prime_factor(number))
    print(largest_prime_factor_old(number))


if __name__ == "__main__":
    main()
