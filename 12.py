#for each triangle, find its factors
#return the first triangle with x number of factors
goal = 500
triangle = 75552778 #triangle for what number?
num = 12292 + 1
factorCount = 0
topFactor = [17907120, 480]

while factorCount <= goal:
    factorCount = 0
    triangle += num

    #for each number below the triangle, add to factorCount if it's a factor of the triangle
    #print str(triangle) + ": ",
    for i in range(1, triangle + 1)[::-1]:
        if triangle % i == 0:
            factorCount += 1
            #print str(i) + ",",

    if factorCount > topFactor[1]:
        topFactor[0] = triangle
        topFactor[1] = factorCount
    print "TOP: " + str(topFactor[0]) + " (" + str(topFactor[1]) + ") ..." + str(triangle) + " (" + str(factorCount) + ") - num: " + str(num)
    num += 1

print "First triangle with over " + str(goal) + " divisors: " + str(triangle)