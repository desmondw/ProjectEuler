maxNum = 100
sumSquares = squareSums = 0

numRange = range(1, maxNum + 1)

for i in numRange:
    sumSquares += pow(i, 2)
    squareSums += i
squareSums = pow(squareSums, 2)

result = squareSums - sumSquares

print str(squareSums) + " - " + str(sumSquares) + " = " + str(result)
