import sys
from cmath import phase, sqrt


def parse_xy(string):
    numbers = string.split('+')
    if len(numbers) == 1:
        numbers = string.split('-')
        print(numbers)
        if len(numbers) == 3:
            x = -float(numbers[1])
            y = -float(numbers[2])
        else:
            x = float(numbers[0])
            y = -float(numbers[1])
    else:
        x = float(numbers[0])
        y = float(numbers[1])
    return x, y



def main():
    x, y = parse_xy(sys.stdin.readline().strip()[:-1])
    print(x)
    print(y)
    ro = abs(sqrt(x*x + y*y))
    phi = phase(complex(x, y))

    print(ro)
    print(phi)


if __name__ == "__main__":
    main()
