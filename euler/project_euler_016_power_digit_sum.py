"""
HackerRank - Problem Name

https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem

2^9 = 512 and the sum of its digits is 5 + 1 + 2 = 8.

What is the sum of the digits of the number 2^N?
"""


def power_digit_sum(n):
    """ Solves the problem"""
    if n == 0:
        return 1
    sumation = 0
    power = 2 << (n - 1)
    for digit in str(power):
        sumation += int(digit)
    return sumation


def main():
    """ main """
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        print(power_digit_sum(n))


if __name__ == "__main__":
    main()
