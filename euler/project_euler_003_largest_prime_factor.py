"""
HackerRank - Project Euler 003

https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N
"""


def get_primes(limit):
    primes = []
    current = list(range(2, limit + 1))
    while current:
        next_prime = current[0]
        primes.append(next_prime)
        current[:] = [num for num in current if num % next_prime != 0]
    return primes


def largest_prime_factor(number):
    primes = get_primes(number)
    for num in reversed(primes):
        if number % num == 0:
            return num


def main():
    """ main """
    # number = 13195
    number = 10
    print(largest_prime_factor(number))


if __name__ == "__main__":
    main()
