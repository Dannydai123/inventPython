"""Bagels, by Danny Dai at dannydai123@gmail.com


prompts:
Pico- One digit is correct but in the  wrong position.
Fermi- One digit is correct and in the right position.
Bagels- No digit is correct.


"""
import random

MAX_TIMES = 10
MAX_DIGITS = 3


def main():
    resultlist = []

    randomNum = str(random.randint(10 ** (MAX_DIGITS - 1), 10 ** MAX_DIGITS) - 1)

    # print(randomNum)

    print("""usage:
Pico- One digit is correct but in the  wrong position.
Fermi- One digit is correct and in the right position.
Bagels- No digit is correct.
         """)
    print(f"you have {MAX_TIMES} times to guess , this number has {MAX_DIGITS} digits.\n")

    for guessTimes in range(MAX_TIMES):

        randomNumList = list(randomNum)

        answerlist = list(input(f"No. {guessTimes} try: please guess a number with {MAX_DIGITS} digits "))

        if set(answerlist) & set(randomNumList):

            resultlist = compare(answerlist, randomNumList)

            if resultlist.count("Fermi") == MAX_DIGITS:
                print("you got a correct number")
                break

        else:
            print("Bagels- No digit is correct")

    print(randomNum)


def compare(answerlist, randomNumList):
    resultlist = []
    for idxans, answerNum in enumerate(answerlist):
        tempresultlist = []
        for idxrandom, randomNum in enumerate(randomNumList):

            if answerNum == randomNum:
                if idxans == idxrandom:
                    tempresultlist.append("Fermi")
                    # print("Fermi", sep=' ')
                else:
                    tempresultlist.append("pico")

        if "Fermi" in tempresultlist:
            print("Fermi", end=' ')
            resultlist.append("Fermi")
        elif "pico" in tempresultlist:
            print("pico", end=' ')

    print()

    return resultlist  # there is resultlist including 3 results of every digit in terms of answer's digit.


if __name__ == '__main__':
    while True:
        main()
        anw = input("Do you want to continue to play, y(es) or n(o)?")
        if anw == 'n':
            break