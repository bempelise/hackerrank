"""
HackerRank - Project Euler 014

www.hackerrank.com/contests/projecteuler/challenges/euler014/problem
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n -> n/2        n is even
n -> 3*n + 1    n is odd

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, <= N produces the longest chain?
If many possible such numbers are there print the maximum one.

Note: Once the chain starts the terms are allowed to go above N.

"""


def longest_collatz_sequence():
    """ Solves the problem"""


def main():
    """ main """
    print(longest_collatz_sequence())


if __name__ == "__main__":
    main()
