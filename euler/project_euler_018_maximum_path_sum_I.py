"""
HackerRank - Maximum path sum I

https://www.hackerrank.com/contests/projecteuler/challenges/euler018/problem

By starting at the top of the triangle below
and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.
The path is denoted by numbers in bold.

    *3*
  *7*  4
 2  4 *6*
8  5 *9* 3

That is, 3 + 7 + 6 + 9 = 23.

Find the maximum total from top to bottom of the triangle given in input.

"""


def recursive(lines, index):
    """ Crashes in 2 test cases """
    if len(lines) == 2:
        left = lines[0][index] + lines[1][index]
        right = lines[0][index] + lines[1][index + 1]
        return max(left, right)
    maximum = max(recursive(lines[1:], index), recursive(lines[1:], index + 1))
    return lines[0][index] + maximum


def maximum_path_sum(lines, depth):
    """ Solves the problem"""
    row = depth - 2
    while row >= 0:
        for i in range(len(lines[row])):
            lines[row][i] += max(lines[row+1][i], lines[row+1][i+1])
        row -= 1
    return lines[0][0]


def main():
    """ main """
    depth = int(input())
    lines = []
    for _ in range(depth):
        lines.append(list(map(int, input().split())))
    print(maximum_path_sum(lines, depth))


if __name__ == "__main__":
    main()
