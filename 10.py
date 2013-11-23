goal = 2000000
num = 3
step = 2

primes = [2]
sum = 2

while num < goal:
    print num
    prime = True
    for i in primes:
        if num % i == 0:
            prime = False
            break
        if i > num / 2:
            break
    if prime:
        primes.append(num)
        sum += num
    num += step

print "The sum of all primes below " + str(goal) + " is " + str(sum)