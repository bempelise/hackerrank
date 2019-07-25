"""
HackerRank - Project Euler 010

https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes not greater than given N.
"""
import time


class Primes():
    """ Class indexing primes """
    def __init__(self, limit):
        self._sums = []
        self._bools = []
        self.sieve(limit)

    def summation(self, limit):
        """ Returns the sum of primes up to limit """
        if limit >= len(self._sums):
            self.sieve(limit)
        return self._sums[limit - 1]

    def sieve(self, number):
        """ Sieve of Eratosthenes """
        number += 1
        self._bools = [True] * number
        self._sums = [0]
        for i in range(2, number):
            if self._bools[i]:
                for j in range(i*i, number, i):
                    self._bools[j] = False
                self._sums.append(self._sums[-1] + i)
            else:
                self._sums.append(self._sums[-1])

        while len(self._sums) < len(self._bools):
            self._sums.append(self._sums[-1])


def benchmark(limit):
    """ Measures efficacy of implementation"""
    start = time.time()
    primes = Primes(limit)
    print(primes.summation(limit))
    end = time.time()
    print("Time elapsed: " + str(end - start))


def diff_with_original():
    """ Used to debuf new implementation """
    primes = Primes(10)
    # primes_orig = PrimesOriginal(10)
    res = 0
    res_orig = 0
    limit = 5
    while res == res_orig:
        res = primes.summation(limit)
        # res_orig = primes_orig.summation(limit)
        limit += 1

    print(limit)
    print(res)
    print(res_orig)


def main():
    """ main """
    limit = 1000
    benchmark(100000)
    primes = Primes(limit)
    print(primes.summation(5))
    print(primes.summation(5))
    print(primes.summation(10))


if __name__ == "__main__":
    main()
