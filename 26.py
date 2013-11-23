from decimal import *

precision = 10000
getcontext().prec = precision
goal = 1000
cyclesToVerify = 3
longestDenominator = 2
longestCycle = 0

def getCycleLength(denominator, num, precision):
    numText = str(num)[2:]

    #filters out numbers with finite decimals
    if len(numText) < precision:
        return None

    pastDecimals = ""
    for i in range(len(numText)): #for each decimal
        for j in range(len(pastDecimals)): #for each demical before the current
            #print "\t[%s] %s... Decimal:%s   %s... PastDecimals:%s" %(denominator, i, numText[i], j, pastDecimals)
            cycle = ""
            fullCycle = True

            for k in range(j, len(pastDecimals)): #for range current past decimal to last past decimal
                step = k - j
                if i + step >= len(numText): #if on last decimal of entire number
                    #print "ERROR: end of decimal string"
                    return None
                if numText[i + step] != pastDecimals[j + step]:
                    fullCycle = False
                    break
                cycle += pastDecimals[j + step]

            if not fullCycle:
                continue

            #compare aqcuired cycle to subsequent digits X number of times
            #print "\tVerifying Cycle '%s'..." %(cycle)
            verified = True
            for step in range(cyclesToVerify):
                start = i + len(cycle) * step
                end = i + len(cycle) * (step + 1)
                if cycle != numText[start:end]:
                    verified = False
                    break
            if verified:
                print "\tVerified! Cycle Length:%s" %(len(cycle))
                return len(cycle)

        pastDecimals += numText[i]

for i in range(2, goal + 1):
    num = Decimal(1) / i
    print ">---Now testing:1/%s (%s)" %(i, num)
    length = getCycleLength(i, num, precision)
    if length > longestCycle:
        longestDenominator = i
        longestCycle = length

print "Winner: (1/%s) with cycle of length %s" %(longestDenominator, longestCycle)