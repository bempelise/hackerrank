"""
"""
ALPHA = 97


def lettersize(size):
    return 4*(size + 1) - 3


def dashsize(size, maxsize):
    return int((maxsize - lettersize(size))/2) - 2


def letterpart(size, maxsize):
    line = ""
    letter = ALPHA + maxsize - 1
    start = letter
    finish = letter - size
    while letter > finish:
        line += chr(letter)
        line += '-'
        letter -= 1
    line += chr(letter)
    letter += 1
    while letter <= start:
        line += '-'
        line += chr(letter)
        letter += 1
    return line


def print_rangoli(size):
    length = lettersize(size)

    for i in range(0, size):
        line = ""
        line += '-'*dashsize(i, length)
        line += letterpart(i, size)
        line += '-'*dashsize(i, length)
        print(line)

    for i in range(size - 2, -1, -1):
        line = ""
        line += '-'*dashsize(i, length)
        line += letterpart(i, size)
        line += '-'*dashsize(i, length)
        print(line)


if __name__ == '__main__':
    # n = int(input())
    print_rangoli(10)
