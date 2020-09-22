"""
HackerRank - Problem Name

https://www.hackerrank.com/contests/projecteuler/challenges/euler017/problem

The numbers 1 to 5 written out in words are One, Two, Three, Four, Five

First character of each word will be capital letter for example:
104382426112 is

One Hundred Four Billion
Three Hundred Eighty Two Million
Four Hundred Twenty Six Thousand
One Hundred Twelve

Given a number, you have to write it in words.

"""

NUM_TO_TEXT = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
}


def decade_to_words(number):
    """ Words for less then 100 """
    return NUM_TO_TEXT[number]


def hundreds_to_words(number):
    """ Words for less than 1000 """
    hundreds = int(number / 100)
    number = number % 100
    tens = int(number / 10)
    number = number % 10

    words = ""
    if hundreds > 0:
        words += NUM_TO_TEXT[hundreds]
        words += " "
        words += "Hundred"
        words += " "

    if tens > 0:
        if tens > 1:
            words += NUM_TO_TEXT[tens*10]
            words += " "
            if number > 0:
                words += NUM_TO_TEXT[number]
                words += " "
        else:
            words += NUM_TO_TEXT[tens*10 + number]
            words += " "
    elif number > 0:
        words += NUM_TO_TEXT[number]
        words += " "

    return words


def step(number, limit, singular):
    words = ""
    # print("number: " + str(number))
    units = int(number / limit)
    # print("units: " + str(units))
    if units > 0:
        words += hundreds_to_words(units)
        words += singular + " "
    return words


def number_to_words(number):
    """ Solves the problem"""
    original = number
    words = ""
    limit = 1000000000000

    words += step(number, limit, "Trillion")
    number = number % limit
    limit /= 1000

    words += step(number, limit, "Billion")
    number = number % limit
    limit /= 1000

    words += step(number, limit, "Million")
    number = number % limit
    limit /= 1000

    words += step(number, limit, "Thousand")
    number = number % limit
    limit /= 1000

    words += hundreds_to_words(number)

    # Zero case
    if words == "":
        words = NUM_TO_TEXT[original]

    return words.strip()


def main():
    """ main """
    number = int(input())
    # number = 104382426112
    print(number_to_words(number))


if __name__ == "__main__":
    main()
