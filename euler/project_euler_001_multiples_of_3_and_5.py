"""
HackerRank - Project Euler 001

https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
https://projecteuler.net/problem=1

If we list all the natural numbers below  10 that are multiples of  3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of  3 or 5 below N.
"""


def mult_sum(limit, number):
    """ Sum of all multiples of given number below limit """
    num_mults = (limit - 1)/number
    sum_mults = (num_mults * (num_mults + 1) / 2) * number
    return sum_mults


def multiples(limit):
    """ Sum of all mMultiples of 3 and 5 below n """
    sum3 = mult_sum(limit, 3)
    sum5 = mult_sum(limit, 5)
    sum15 = mult_sum(limit, 15)
    sum_all = sum3 + sum5 - sum15
    return sum_all


def main():
    """ main """
    cases = [100]
    for case in cases:
        print(multiples(case))


if __name__ == "__main__":
    main()
