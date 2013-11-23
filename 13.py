import re

file = open("13_data.txt")
sum = 0

while True:
    line = re.search(r".*", file.readline()).group(0)
    print line
    if line == "":
        break
    sum += int(line)

print "\nSum:"
print sum
print "\nFirst 10 digits of sum: " + str(sum)[:10]