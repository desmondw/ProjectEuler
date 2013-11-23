import re

size = 9
routeCount = 0
path = "1" * size + "0" * size

def nextPath():
    global path
    m = re.search("1"*size, path)
    if m is not None: #if all the 1s are in a row
        if m.end() == len(path): #if all the 1s are at the end
            return False #end
        #else move last 1 a char right and the other 1s to the far left
        path = "1"*(size-1) + "0"*(size+1)
        path = path[:m.end()] + "1" + path[m.end()+1:]
    else: #find first 10 and swap it with 01
        m = re.search("1+0", path)
        if len(m.group(0)) == 2 or m.start() == 0:
            m = re.search("10", path)
            path = path[:m.start()] + "01" + path[m.end():]
        else:
            onesAmount = len(path[m.start():m.end()-2])
            path = path[m.start():m.end()-2] + "0"*(m.start()+1) + "1" + path[m.end():]
    return True

notDone = True
while notDone:
    print path
    routeCount += 1
    notDone = nextPath()

print "Routes in a %sx%s: %s" %(size, size, routeCount)