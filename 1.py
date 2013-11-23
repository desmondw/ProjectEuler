sum = 0

print sum
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        print str(i) + " + " + str(sum - i) + " = " + str(sum)
