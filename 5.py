import sys

def smallEvenFactors(num):
    maxDiv = 20
    step = maxDiv * 19 * 17 * 13 * 11
    num = step
    #divRange = range(2, maxDiv + 1)[::-1]
    divRange = [18, 16, 15, 14, 12]

    while True:
        print num
        for i in divRange:
            if num % i != 0:
                break
            elif i == divRange[len(divRange) - 1]:
                print str(num) + " is evenly divisible by a factorial of " + str(maxDiv) + "!"
                return num

        num += step

smallEvenFactors(10)