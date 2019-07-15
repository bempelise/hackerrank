"""
HackerRank - Project Euler 005

www.hackerrank.com/contests/projecteuler/challenges/euler006/problem
https://projecteuler.net/problem=6


The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,(1 + 2 + ... 10)^2 = 3025.
Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the absolute difference between the sum of the squares of the first N natural numbers
and the square of the sum.
"""


def sum_of_squares(limit):
    """ Returns the sum of the squares of the numbers up to limit """
    value = 0
    for i in range(1, limit + 1):
        value += i * i
    return value


def square_of_sums(limit):
    """ Returns the square of the sum of the numbers up to limit """
    value = 0
    for i in range(1, limit + 1):
        value += i
    return value * value


def sum_square_difference(limit):
    """ Returns the absolute difference between the squares of
        the first numbers up to limit and the square of their sum
    """
    sum_square = sum_of_squares(limit)
    square_sum = square_of_sums(limit)
    return abs(sum_square - square_sum)


def main():
    """ Main """
    limit = 10
    print(sum_square_difference(limit))


if __name__ == "__main__":
    main()
