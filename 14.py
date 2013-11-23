num = 1000000
n = num - 1
counter = largestCounter = largestNum = 0

for i in range(1, num)[::-1]:
    counter = 0
    n = i
    print i
    while n > 1:
        if n % 2 == 0: #even
            n = n / 2
        else: #odd
            n = 3*n + 1
        counter += 1
    if counter > largestCounter:
        largestCounter = counter
        largestNum = i
print "The number below " + str(num) + " that creates the longest chain: " + str(largestNum)