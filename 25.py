a, b = 1, 1
counter = 2
while True:
    a, b = b, a+b
    counter += 1
    length = len(str(b))
    print "Length of b " + str(length)
    if length >= 1000: #if 1000 digits long
        print "First term with 1000 digits: " + str(counter)
        break