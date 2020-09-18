"""
HackerRank - Lattice Paths

https://www.hackerrank.com/contests/projecteuler/challenges/euler015/problem

Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a NxM grid?
As number of ways can be very large, print it modulo (10^9 + 7).
"""

from math import factorial

MODULO = 1000000000 + 7


def main():
    """ main """
    # tests = int(input())
    # for _ in range(tests):
    #     pairs = input().strip().split(' ')
    #     m = int(pairs[0])
    #     n = int(pairs[1])
    #     print(lattice_paths(m, n))
    print(lattice_paths(3, 3))  # 20
    print(lattice_paths(2, 2))  # 6
    print(lattice_paths(3, 2))  # 10
    print(lattice_paths(2, 3))  # 10


def lattice_paths(m, n):
    """ Solves the problem"""
    return factorial(m + n) // (factorial(m) * factorial(n)) % MODULO


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    main()


def binomial_calculation(n, m):
    """ From the web"""
    p = int(1e9+7)  # NOTE: the conversion is important
    def exp_mod(a, n):
        if n == 0:
            return 1
        temp = exp_mod(a, n // 2)
        if n % 2 == 0:
            return (temp * temp) % p
        return (temp * temp * a) % p

    factor = [1]
    inv_factor = [1]

    for i in range(1, m + n + 1):
        factor.append((factor[i-1] * i) % p)
        inv_factor.append((inv_factor[i-1] * exp_mod(i, p-2)) % p)

    return (factor[n+m] * inv_factor[n] * inv_factor[m]) % p
