
sum = 1
goal = 1001
#for i in range(3, goal):
i = 3
while i <= goal:
    num = pow(i, 2)
    sum += num * 4 - (i - 1) * 6
    print "i: " + str(i) + " num: " + str(num)
    i += 2
print "Sum: " + str(sum)