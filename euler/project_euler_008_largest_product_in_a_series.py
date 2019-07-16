"""
HackerRank - Project Euler 008

https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem
https://projecteuler.net/problem=8

Find the greatest product of K consecutive digits in the N digit number.
"""


def product(buffer):
    """ Returns the product of the buffer contents """
    prod = 1
    for num in buffer:
        prod *= num
    return prod


def largest_product(number, window):
    """ Returms the greatest sum of consecutive digits
        of the given number within a given window
    """
    string = str(number)
    maximum = 0
    index = 0
    buffer = [0] * window

    for char in string:
        buffer[index] = int(char)
        prod = product(buffer)
        index += 1
        if index >= window:
            index = 0
        print(str(buffer) + " / " + str(prod))
        if prod > maximum:
            maximum = prod
    return int(maximum)


def main():
    """ main """
    number = 3675356291
    number = 2709360626
    print(largest_product(number, 5))


if __name__ == "__main__":
    main()
