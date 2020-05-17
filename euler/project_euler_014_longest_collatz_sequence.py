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
CACHE_SIZE = 5000
CACHE = [0] * CACHE_SIZE
CACHE[0] = 1


def collatz(num):
    if num < CACHE_SIZE and CACHE[num - 1] != 0:
        return CACHE[num - 1]

    if num % 2:
        result = 1 + collatz(3*num + 1)
    else:
        result = 1 + collatz(num >> 1)
    if num < CACHE_SIZE:
        CACHE[num - 1] = result
    return result


for num in range(2, CACHE_SIZE):
    collatz(num)

SOLUTIONS = [
    3732423,
    3542887,
    3064033,
    2298025,
    1723519,
    1564063,
    1501353,
    1126015,
    1117065,
    837799,
    837799,
    626331,
    511935,
    410011,
    230631,
    216367,
    156159,
    142587,
    106239,
    77031,
    52527,
    35655,
    35497,
    34239,
    26623,
    23529,
    17673,
    17647,
    13255,
    10971,
    6171,
    3711,
    2919,
    2463,
    2323,
    2322,
    2223,
    1161,
    871,
    703,
    667,
    655,
    654,
    649
]


def main():
    """ main """
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(longest_collatz_sequence(n))


def longest_collatz_sequence(number):
    """ Solves the problem"""
    index = 0
    while index < len(SOLUTIONS):
        if number >= SOLUTIONS[index]:
            return SOLUTIONS[index]
        index += 1

    longest = 1
    index = 1
    for i in range(1, number + 1):
        current = CACHE[i - 1]
        if current >= longest:
            longest = current
            index = i
    return index


if __name__ == "__main__":
    main()
