a, b = 1, 2
sum = 0
while b < 4000000:
    print "a:" + str(a) + " b:" + str(b),
    if b % 2 == 0:
        sum += b
    print " sum:" + str(sum)
    a, b = b, a+b
    
