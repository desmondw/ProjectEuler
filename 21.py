goal = 10000
amicablePairs = []
sumsOfDivisors = [0, 0, 1]

def sumOfDivisors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

def isAmicablePair(a, b):
    if sumsOfDivisors[a] == b and sumsOfDivisors[b] == a:
        return True
    return False

for a in range(3, goal):
    sumsOfDivisors.append(sumOfDivisors(a))
    print "a:%s, +/:%s" %(a,sumsOfDivisors[a])
    for b in range(2, a):
        if isAmicablePair(a, b):
            amicablePairs.append(a)
            amicablePairs.append(b)
            print "ADDED %s, %s" %(a,b)

cleanPairs = []
sum = 0
for i in amicablePairs:
    duplicate = False
    for j in cleanPairs:
        if i == j:
            duplicate = True
            break
    if not duplicate:
        cleanPairs.append(i)
        sum += i

print "Amicable pairs: " + str(cleanPairs)
print "Sum of amicable numbers: " + str(sum)