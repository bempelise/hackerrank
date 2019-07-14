"""
HackerRank - Project Euler 004

https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The smallest 6 digit palindrome made from the product of
two 3-digit numbers is 101101 = 143 * 707.

Find the largest palindrome made from the product
of two 3-digit numbers which is less than N.
"""

import math


def hasThreeDigitFactors(number):
    """ Returns true if he number has 2 three digit factors """
    first = math.ceil(number / 1000)
    if first < 100:
        return False
    while True:
        # Get next divisor
        while number % first != 0:
            first += 1
            if first >= 1000:
                return False

        second = number / first
        if 99 < second < 1000:
            return True


def is_palindrome(number):
    """ Returns true if the number is a palindrome """
    string = str(number)
    for i in range(3):
        if string[i] != string[-1 - i]:
            return False
    return True


def largest_palindrome(number):
    """ Returns the largest palindrome less than thie given number """
    number -= 1
    if not 101101 <= number < 1000000:
        return None
    while not (is_palindrome(number) and hasThreeDigitFactors(number)):
        number -= 1
    return number


def main():
    """ Main """
    number = 999999
    number = 100000
    print(largest_palindrome(number))
    # while number and number > 100000:
    #     number = largest_palindrome(number)
    #     print(number)
    #     number -= 1


if __name__ == "__main__":
    main()
