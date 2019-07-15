"""
HackerRank - Project Euler 007

www.hackerrank.com/contests/projecteuler/challenges/euler007/problem
https://projecteuler.net/problem=7

By listing the first six prime numbers:
2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the Nth prime number?
"""


def get_primes(limit):
    """ Get all primes below limit """
    primes = []
    current = list(range(2, limit + 1))
    while current:
        next_prime = current[0]
        primes.append(next_prime)
        current[:] = [num for num in current if num % next_prime != 0]
    return primes


class Primes():
    """ Class indexing primes """
    def __init__(self):
        # 10001st prime limit:  n(ln(n) + ln (ln(n))) = 114319
        self._primes = get_primes(114319)

    def prime_at(self, index):
        """ Returns Nth prime """
        return self._primes[index - 1]


def main():
    """ main """
    primes = Primes()
    n = 6
    print(primes.prime_at(n))


if __name__ == "__main__":
    main()
