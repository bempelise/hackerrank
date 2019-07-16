"""
HackerRank - Project Euler 010

https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes not greater than given N.
"""


class Primes():
    """ Class indexing primes """
    def __init__(self, limit):
        self._limit = 2
        self._primes = []
        self.extend(limit)

    def prime_at(self, index):
        """ Returns (N+1)th prime """
        return self._primes[index]

    def extend(self, limit):
        """ Get all primes below limit """
        limit += 1
        if self._limit >= limit:
            return

        current = list(range(self._limit, limit + 1))
        for prime in self._primes:
            current[:] = [num for num in current if num % prime != 0]

        while current:
            next_prime = current[0]
            self._primes.append(next_prime)
            current[:] = [num for num in current if num % next_prime != 0]
        self._limit = limit

    def size(self):
        """ Returns the size of the primes numbers held"""
        return len(self._primes)


def summation_primes(primes, number):
    """ Returns the sum of all prims below number"""
    summation = 0
    index = 0
    print(primes._primes)
    while index < primes.size() and primes.prime_at(index) <= number:
        summation += primes.prime_at(index)
        index += 1
    return summation


def main():
    """ main """
    primes = Primes(10)
    number = 5
    primes.extend(number)
    print(summation_primes(primes, number))
    number = 10
    primes.extend(number)
    print(summation_primes(primes, number))


if __name__ == "__main__":
    main()


