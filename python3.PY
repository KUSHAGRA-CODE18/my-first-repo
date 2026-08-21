"""
str1 = "This is a string "
str2 = 'Kushagra Vaish'
str3 = '''this is a string'''
str4 = '''This is a multy line string \n we are creating it in python.'''

print(str1)
print(str2)
print(str3)
print(str4)
str5 = str1 + str2
print(str5)
print(len(str1+str2))
"""

'''
p=str1[5]
print(p)

str1[5]='s'# ITEM ASSIGNMENT DOES NOT POSSIBLE IN STRING.
print(str1)
'''

'''
st = "Kushagra Vaish"
print(st[0:5])
print(st[2:9])
print(st[5:len(st)])
print(st[:8])
print(st[-3:-2])
print(st[-8:])
'''

'''
st = "i am sthudying python"

print(st.endswith("on"))
print(st.endswith("uhi"))

st1 = print(st.capitalize())
print(st)
print(st1)

print(st.replace("y","x"))
print(st.replace("am", "was"))

print(st.find("y"))
print(st.find("th"))
print(st.find("q"))

print(st.count("th"))
'''

'''
name = str(input("Enter your name : "))
print("Length of your name :",len(name))
'''

'''
st = "$ is the currency of USA. 1$=Rs.95.65. That's why I hate $"
print(st.find("$"))
print(st.count("$"))
'''

#IF-ELIF-ELSE CONDITION

'''
age = int(input("Enter your age :"))
if (age >= 18 and age < 75):
    print("can vote") # Indentation[VERY IMPORTANT]
    print("can drive")
elif (age < 18):
    print("can not vote")
    print("can not drive")
else:
    print("Too old for driving. Don't Drive!!")
'''

'''
num1 = int(input("Enter the 1st no. :"))
num2 = int(input("Enter the 2nd no. :"))
num3 = int(input("Enter the 3rd no. :"))
if (num1 > num2 and num1 > num3):
    print(num1,"is greatest")
elif (num2 > num1 and num2 > num3):
    print(num2,"is greatest")
else:
    print(num3,"is greatest")
'''

