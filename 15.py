#answer = 2^(size*2) - (1 + sum(size*2^n) + n - 1)
"""
size = 3
answer = 2 ** (size*2)
answer -= 2
for n in range(1, size):
    answer -= size * 4 ** n + n - 1
print answer
"""
def myRange(stop):
    i = 0
    while i < stop:
        yield i
        i += 1

size = 20
routeCount = 0

for i in myRange(2**(size*2)):
    binary = bin(i)[2:]
    print binary

    onesCount = 0
    for j in range(len(binary)):
        if binary[j] == "1":
            onesCount += 1
    if onesCount == size:
        routeCount += 1

print "Routes in a %sx%s: %s" %(size, size, routeCount)