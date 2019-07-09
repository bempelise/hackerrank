"""
Rho algorithm to find non-trivial prime factors
https://en.wikipedia.org/wiki/Pollard's_rho_algorithm
"""

import math


def gcd(a, b):
    """ Eucledes algorithm to calculate the GCD between a and b"""
    while a % b != 0:
        a, b = b, a % b
    return b


def is_perfect_square(number):
    """ Returns true of the given number is a perfect square """
    sqrt = math.sqrt(number)
    return not sqrt - math.floor(sqrt) > 0.0


def g(x, number):
    """ Rho Polynomial """
    return x*x + 1 % number


def get_factor(number, x)
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
    """ WIP: The idea is to get the largest prime factor obained by Rho algorithm"""
    if number in [1, 0]:
        return None

    # Rho's algorithm does not work with squares
    while is_perfect_square(number):
        number = number / int(math.sqrt(number))

    max_factor = None
    sqrt = math.sqrt(number)
    for i in range(int(sqrt)):
        factor = get_factor(number, i)
        if max_factor is None or factor > max_factor:
            max_factor = factor
    return max_factor


def print_factors(number):
    """ Prints the output of Rho algorithm.
        Auxiliary debug function
    """
    sqrt = math.sqrt(number)
    for i in range(int(sqrt)):
        print("{}: {}".format(i, get_factor(number, i)))


def main():
    """ Main """
    number = 217
    print(largest_prime_factor(number))


if __name__ == "__main__":
    main()
