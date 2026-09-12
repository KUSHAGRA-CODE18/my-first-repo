#STRING IN PYTHON
#1. split()
'''

Ex. Splitting a string in python


message = "Python Programming language"
n = message.split()
print("before splitting: ", message)
print("After splitting: ", n)

message2 = "python programming language, python is easy to learn"
m = message2.split(",")
print(m)
'''

'''
s1 = "13:25:09"
h, m, s = s1.split(":")[0], s1.split(":")[1], s1.split(":")[2]
print(h)
print(m)
print(s)
'''




#2. join()
'''
We can join a group of strings (list or tuples) w.r.t. the given operator

Ex. separator is "-" symbol joining group of string in the give list

l1 = ["Rajesh","Jai","Rohit","Chetan"]
s1 = '-'.join(l1)
print(s1)
print(type(s1))
'''




'''
name = "raj"
s = input("Enter Fixed name: ")
if name == s:
    print("OK")
else:
    print("Don't be so smart,😏")

name = "Rohan is a genius"
print(name.lower())
print(name.upper())
print(name.swapcase())
print(name.title())
print(name.capitalize())
'''

'''
name = "Rohan is a genius"
print(name.isalnum())
print(name.isalpha())

val = input("Enter Value: ")
val = val if val.isalpha() else eval(val)
print(val)
print(type(val))
'''


'''
name  = "Rohit"
age = 18
place = "Delhi"
subs = "{} lives in {} and his age is {}".format(age, name, place)
print(subs)

subs = "{1} lives in {2} and his age is {0}".format(age, name, place)
print(subs)

subs = "{n} lives in {p} and his age is {a}".format(a = age, n = name, p = place)
print(subs)
'''


'''
name  = "Rohit"
age = 18
place = "Delhi"
subs = f"{name} lives in {place} and his age is {age}"
print(subs)

'''