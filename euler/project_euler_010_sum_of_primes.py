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


class CacheEntry():
    def __init__(self, value, index):
        self._value = value
        self._index = index

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def index(self):
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

def main():
    """ main """
    primes = Primes(10)
    adder = PrimeAdder(primes)
    number = 5
    print(adder.summation(number))
    number = 10
    print(adder.summation(number))


if __name__ == "__main__":
    main()


