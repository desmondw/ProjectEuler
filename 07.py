primes = [2]
num = 3
step = 2
goal = 10001

while len(primes) < goal:
    print num
    prime = True
    for i in primes:
        if num % i == 0:
            prime = False
            break
    if prime:
        primes.append(num)
    num += step

print "The #" + str(goal) + " prime is: " + str(primes[len(primes)-1])