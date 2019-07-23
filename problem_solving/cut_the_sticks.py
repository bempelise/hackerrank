"""
HackerRank - Cut the sticks

www.hackerrank.com/challenges/cut-the-sticks/problem
"""


def cut_the_sticks(arr):
    """ Cut the sticks """
    ret = []
    while arr:
        if not ret or len(arr) != ret[-1]:
            ret.append(len(arr))
        cut = min(arr)
        arr[:] = [(num - cut) for num in arr if num > 0]
    return ret


def main():
    """ main """
    input = [1, 2, 3, 4, 3, 3, 2, 1]
    print(cut_the_sticks(input))


if __name__ == "__main__":
    main()
