from datetime import datetime,date
from pprint import pprint
from random import randint

""" 
The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. In a group of 70 people, there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday.
"""

def getbirthdays(count, isverbose):

    resultlist = []

    for i in range(count):
        initDate = date(2000,1,1).toordinal()     # 730120

        resultlist.append(date.fromordinal(randint(initDate, initDate + 364)))
    if isverbose:
        print(f"here are {count} birthdays :")

        for birthday in resultlist:

            print(birthday.strftime("%b %d"), end=', ')

        print()


    return resultlist


def findSameBirthday(bdaylist, isverbose=False):

    templist = []


    for bday in bdaylist:

        if bday not in templist:
            templist.append(bday)
        elif bday in templist and  isverbose:
            print("In this simulation, multiple people have a birthday on ", bday.strftime("%b %d"))
            return bday

        elif bday in templist and not isverbose:
            return bday #in simulations


    return None


def main():


    SIMULATIONS = 100000

    BIRTHDAY_MAX_COUNT = int(input("How many birthdays shall I generate? (Max 100)"))



    birthdaylist = getbirthdays(BIRTHDAY_MAX_COUNT, isverbose=True)

    if not findSameBirthday(birthdaylist, isverbose=True):
        print("there is no matching birthday")


    def simulations():

        matchingbdayCount = 0

        input(f"Generating {BIRTHDAY_MAX_COUNT} random  birthdays {SIMULATIONS} times...  Press Enter to begin...")

        for simulationCount in range(0, SIMULATIONS):

            birthdaylist = getbirthdays(BIRTHDAY_MAX_COUNT, isverbose=False)
            matchingbdayCount += 1 if findSameBirthday(birthdaylist, isverbose=False) else 0

            if simulationCount % (SIMULATIONS//10) == 0:
                print(simulationCount, "simulations run...")

        print(matchingbdayCount, f"{round(matchingbdayCount/SIMULATIONS * 100, 2)}%")

    simulations()


if __name__ == '__main__':
    main()