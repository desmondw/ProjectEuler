import re
fileString = open("22_names.txt").read()
print fileString
pattern = "\W+"
names = re.split(pattern, fileString[1:-1])
print names
names = sorted(names)
print names
totalSum = 0
for i in range(0, len(names)):
    sum = 0
    for letter in names[i]:
        sum += ord(letter) - 64
    totalSum += sum * (i+1)

print totalSum