a = 0
b = 1
c = 2
goal = 1000

def pythTrip():
    global a, b, c, goal
    while True:
        for i in range(0, c)[::-1]:
            for j in range(0, b)[::-1]:
                print str(a) + ", " + str(b) + ", " + str(c)
                if a + b + c == goal and pow(a, 2) + pow(b, 2) == pow(c, 2):
                    return
                a+= 1
            b += 1
            a = 0
        c += 1
        b = 0
        a = 0

pythTrip()
print "\nRESULT... "
print str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2 ...and " + str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c)
print str(a) + " * " + str(b) + " * " + str(c) + " = " + str(a*b*c)