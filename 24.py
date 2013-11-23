digits = []
count = 0

def calcLex():
    global count, digits
    for num in range(10):
        if count == 1000000:
            return
        if num in set(digits):
            continue
        digits.append(num)

        #tests if lex has been made
        if len(digits) == 10:
            count += 1
            print str(digits) + " #" + str(count)
            if count == 1000000:
                print "DONE!"
        else:
            calcLex()

        digits.remove(num)

calcLex()