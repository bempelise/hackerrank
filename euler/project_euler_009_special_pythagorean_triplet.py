"""
HackerRank - Project Euler 009

https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

Given N, Check if there exists any Pythagorean triplet for which a + b + c = N
Find maximum possible value of a*b*c among all such Pythagorean triplets,
If there is no such Pythagorean triplet print -1.

"""

from collections import namedtuple
PythagoreanTriplet = namedtuple('PythagoreanTriplet', 'a b c')


def get_triplet(m, n):
    """ Returns a Pythagorean Triplet using Euclid's formula """
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n
    return PythagoreanTriplet(a, b, c)


def triplet_sum(triplet):
    """ Returns the sum of a triplet factors """
    return triplet.a + triplet.b + triplet.c

def triplet_product(triplet):
    """ Returns the product of a triplet factors """
    return triplet.a * triplet.b * triplet.c


def find_triplets(number):
    """ Returns a list of pythagorean triplets with sum equal to number """
    factor_m = 2
    factor_n = 1
    triplets = []
    while True:
        triplet = get_triplet(factor_m, factor_n)
        tsum = triplet_sum(triplet)
        if number % tsum == 0:
            factor = number / tsum
            triplets.append(PythagoreanTriplet(triplet.a * factor,
                                               triplet.b * factor,
                                               triplet.c * factor))
            factor_m += 2
        # below number, increase m
        elif tsum < number:
            factor_m += 2
        # above number, increase n and reset m
        elif factor_m != factor_n + 1:
            factor_n += 1
            factor_m = factor_n + 1
        # above number but m has not changed so n suffices to get us over number
        else:
            break

    return triplets


def get_max_triplet_product(number):
    """ Returns the maximum product of a Pythagorean triplet
        with sum equal to number, -1 if none found
    """
    triplets = find_triplets(number)
    if not triplets:
        return -1

    max_product = 0
    for triplet in triplets:
        product = triplet_product(triplet)
        if product > max_product:
            max_product = product
    return int(max_product)


def main():
    """ Main """
    number = 12
    print(get_max_triplet_product(number))
    number = 4
    print(get_max_triplet_product(number))

if __name__ == "__main__":
    main()
