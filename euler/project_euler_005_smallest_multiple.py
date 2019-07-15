"""
HackerRank - Project Euler 005

https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
(divisible with no remainder) by all of the numbers from 1 to N?
"""


def factorial(number):
    """ Returns the factorial of the number """
    if number in [0, 1]:
        return 1
    return number * factorial(number - 1)


def number_divisible(number, limit):
    """ Returns true if the number is divisible by all numbers """
    for i in range(2, limit + 1):
        if number % i != 0:
            return False
    return True


def smallest_multiple(limit):
    """ Returns the smallest number that has as factors
        all the number from 1 to number
    """
    number = factorial(limit)
    divisor = 2
    while divisor <= limit:
        while number_divisible(number, limit):
            number /= divisor
        number *= divisor
        divisor += 1
    return int(number)


def main():
    """ Main """
    limit = 10
    limit = 3
    print(smallest_multiple(limit))


if __name__ == "__main__":
    main()
