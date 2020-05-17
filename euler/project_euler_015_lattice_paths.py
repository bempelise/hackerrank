"""
HackerRank - Lattice Paths

https://www.hackerrank.com/contests/projecteuler/challenges/euler015/problem

Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a NxM grid?
As number of ways can be very large, print it modulo (10^9 + 7).
"""

import math

MODULO = 1000000000 + 7


def main():
    """ main """
    # tests = int(input())
    # for _ in range(tests):
    #     pairs = input().strip().split(' ')
    #     m = int(pairs[0])
    #     n = int(pairs[1])
    #     print(lattice_paths(m, n))
    print(lattice_paths(3, 3))  # 184
    print(lattice_paths(2, 2))  # 6
    print(lattice_paths(3, 2))  # 10
    print(lattice_paths(2, 3))  # 10


def lattice_paths(m, n):
    """ Solves the problem"""
    combinations = int(math.pow((m + 1), n))
    duplicates = int(math.floor((combinations - (m + 1)) /n))
    return (combinations - duplicates) % MODULO




if __name__ == "__main__":
    main()
