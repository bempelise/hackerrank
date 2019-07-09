"""
HackerRank - Project Euler 003

https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N
"""

import math


def get_maxfactor(number):
    """ Return the maximum prime factor of given number"""
    max_factor = 1
    while (number % 2) == 0:
        max_factor = 2
        number /= 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while (number % i) == 0:
            max_factor = i
            number /= i

    # if it is still more than 2 it is a prime itself
    if number > 2:
        max_factor = number

    return int(max_factor)


def main():
    """ main """
    number = 13195
    number = 10416
    number = 9
    # number = 217
    print(get_maxfactor(number))


if __name__ == "__main__":
    main()
