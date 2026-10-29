#                           FUNCTION RECURSIONS

# Ques1:
def sumofdigits(number):
    if number == "":
        return 0
    else:
        return int(number[0]) + sumofdigits(number[1:])
print(sumofdigits("12345"))

# Ques2:
def sumofdigits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sumofdigits(number // 10) 
print(sumofdigits(12345))

# Ques3:
def power(number, powr):
    if powr == 0:
        return 1
    else:
        return number * power(number, (powr-1))
print(power(2, 3))

# Ques4:
def addnum(number, sum):
    if number == 0:
        return sum
    else:
        return addnum(number // 10, sum+(number%10))
print(addnum(1234, 0))

# Ques5:
def reverse(str, rev):
    if not str:
        return rev
    else:
        return reverse(str[1:], str[0]+rev)
print(reverse("Kushagra", ""))

# Write a recursive function To find whether the string is a palindrome or not.

def ispallindrome(str, end, start):
    if start == end:
        return True
    elif str[start] != str[- (start + 1)]:
        return False
    else:
        return ispallindrome(str, end, start + 1)
print(ispallindrome("mada", len("mada"), 0))