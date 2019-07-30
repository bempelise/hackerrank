"""
HackerRank - Project Euler 013

www.hackerrank.com/contests/projecteuler/challenges/euler013/problem
https://projecteuler.net/problem=13

Work out the first ten digits of the sum of N 50-digit numbers.


"""


def large_sum(numbers):
    """ Returns the first 10 digits of the sum of N 50-digit numbers"""
    summation = 0
    for number in numbers:
        summation += number

    while summation > 10**10:
        summation /= 10

    return int(summation)


def main():
    """ main """
    numbers = [
        37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
    ]
    print(large_sum(numbers))

    # size = int(input().strip())
    # numbers = []
    # for _ in range(size):
    #     numbers.append(int(input().strip()))
    # print(large_sum(numbers))


if __name__ == "__main__":
    main()
