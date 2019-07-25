"""
HackerRank - Project Euler 010

https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes not greater than given N.
Original implementation
"""


def find(number, primes, sums):
    """ Find the largest prime less than the number and return equivalent sum """
    index = int(len(primes)/2)
    if index + 1 == len(primes) or primes[index] < number < primes[index + 1]:
        return sums[index]
    if primes[index] > number:
        return find(number, primes[:index], sums[:index])
    if primes[index] < number:
        return find(number, primes[index:], sums[index:])
    return sums[index]


class PrimesOriginal():
    """ Class indexing primes """
    def __init__(self, limit):
        self._limit = 2
        self._primes = []
        self._sums = []
        self.extend(limit)

    def prime_at(self, index):
        """ Returns (N+1)th prime """
        return self._primes[index]

    def summation(self, limit):
        """ Returns the sum of primes up to limit """
        if self._limit < limit:
            self.extend(limit)
        return find(limit, self._primes, self._sums)

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
            if not self._sums:
                self._sums.append(next_prime)
            else:
                self._sums.append(self._sums[-1] + next_prime)
            current[:] = [num for num in current if num % next_prime != 0]
        self._limit = limit


class CacheEntry():
    """ Class holding prime sums and indexes """
    def __init__(self, value, index):
        self._value = value
        self._index = index

    @property
    def value(self):
        """ Value of sum """
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def index(self):
        """ Index of sum """
        return self._index

    @index.setter
    def index(self, value):
        self._index = value


class PrimeAdder():
    """ Gives sum of all primes below a number. Caches old results """
    def __init__(self, primes):
        self.primes = primes
        self.cache = {}

    def summation(self, number):
        """ Returns the sum of primes up to limit """
        if number in self.cache.keys():
            return self.cache[number].value
        self.primes.extend(number)
        entry = self.load_last(number)
        while entry.index < self.primes.size() and self.primes.prime_at(entry.index) <= number:
            entry.value += self.primes.prime_at(entry.index)
            entry.index += 1

        self.cache[number] = entry
        return entry.value

    def load_last(self, number):
        """ Searches for the cached sum to return
            (bad implementation look find() above)
        """
        keys = list(self.cache.keys()).sort()
        if not keys:
            return CacheEntry(0, 0)
        size = len(keys)
        summation = 0
        index = 0

        i = size/2
        while 0 < i < size - 1:
            if number > keys[i]:
                summation = self.cache[keys[i]].value
                index = self.cache[keys[i]].index
                i = i + (size - i)/2
            else:
                if summation > 0:
                    break
                i = i/2
        return CacheEntry(summation, index)
