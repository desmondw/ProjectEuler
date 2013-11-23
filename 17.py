def getNumText(num):
    if num == 0:
        return ""
    elif num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"

def getNumTextTeens(num):
    if num == 10:
        return "ten"
    elif num == 11:
        return "eleven"
    elif num == 12:
        return "twelve"
    elif num == 13:
        return "thirteen"
    elif num == 14:
        return "fourteen"
    elif num == 15:
        return "fifteen"
    elif num == 16:
        return "sixteen"
    elif num == 17:
        return "seventeen"
    elif num == 18:
        return "eighteen"
    elif num == 19:
        return "nineteen"

def getNumTextTens(num):
    text = ""
    if num >= 90:
        text =  "ninety"
    elif num >= 80:
        text =  "eighty"
    elif num >= 70:
        text =  "seventy"
    elif num >= 60:
        text =  "sixty"
    elif num >= 50:
        text =  "fifty"
    elif num >= 40:
        text =  "forty"
    elif num >= 30:
        text =  "thirty"
    elif num >= 20:
        text =  "twenty"
    return text + getNumText(num % 10)

def getCharCount(num):
    text = ""
    if num >= 1000:
        text += "onethousand"
    if num >= 100:
        if num % 1000 >= 100: #if there is a hundreds place
            text += getNumText(int(str(num)[-3]))
            text += "hundred"
        if num % 100 != 0:
            text += "and"

    num = int(str(num)[-2:]) #gets last two digits

    if num >= 20:
        text += getNumTextTens(num)
    elif num >= 10:
        text += getNumTextTeens(num)
    else:
        text += getNumText(num)
    print text
    return len(text)

max = 1000
min = 1
sum = 0
for i in range(min, max+1):
    sum += getCharCount(i)
print "Sum of written characters for numbers " + str(min) + " to " + str(max) + " (inclusive) is: " + str(sum)

#print "Sum of written characters for " + str(max) + " is: " + str(getCharCount(max))