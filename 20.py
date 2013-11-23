import math

text = str(math.factorial(100))
print text
sum = 0
for i in text:
    sum += int(i)
print sum