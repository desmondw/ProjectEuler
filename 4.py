import sys
maxNum = 999
minNum = 100

def checkPalindrome(num):
    if (str(num) == str(num)[::-1]):
        return True
    return False
        
num1 = num2 = maxNum
palindromes = []
while num1 >= minNum:
    while num2 >= minNum:
        print str(num1) + " * " + str(num2) + " = " + str(num1 * num2)
        if (checkPalindrome(num1 * num2)):
            palindromes.append(num1 * num2)
        num2 -= 1
    num1 -= 1
    num2 = maxNum

palindromes.sort()
print("Largest palindrome: " + str(palindromes[-1]))
