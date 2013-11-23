def isPrime(num):
    lowers = range(2, num)
    lowers.reverse()
    for i in lowers:
        if num % i == 0:
            return False
    return True

#generate primes below 1000
primes = []
for i in range(2, 10000):
    print "Checking prime... " + str(i),
    if isPrime(i):
        primes.append(i)
        print " PRIME"
    else:
        print

num = 600851475143
factors = []

def getFactors(num):
    for i in primes:
        print "Checking if factor... " + str(i),
        if num % i == 0:
            factors.append(i)
            print " YES!"
            return num / i
        else:
            print
    return num

while num > 1:
    num = getFactors(num)

print "\n\nFactors:"
for i in factors:
    print i
