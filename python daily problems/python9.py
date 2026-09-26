# COPYING/CLONNING IN LIST
#1. Shallow copy:
#2. Deep copy
x = [10, 20, 30]
y = x
print(x)
print(y)
print(id(x), id(y))
x[1] = 99
print(x)
print(y)
print(id(x), id(y))

a = [10, 20, 30]
b = a.copy()
print(a)
print(b)
print(id(x), id(y))

#Mathematical Operators on list 
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# a = [1, 2, 3]
# b = "Ramesh" # here 'typeerror' will occur. 
# c = a + b
# print(c)

a = [1, 2, 3]
print(a * 2)

#Comparison of list in Python 

print([1, 2, 3] < [2, 2, 3])
print([1, 2, 3] < [1, 2, 3])
print([1, 2, 3] <= [2, 2, 3])
print([1, 2, 3] < [1, 2, 4])
print([1, 2, 3] < [0, 2, 3])
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [1, 2, 3])

#While comparing lists that are loaded with strings, the following things are considered for the comparison:
# 1. The number of elements
# 2. The order of elements
# 3. The content of elements (case-sensitive)

x = ["abc", "def", "ghi"]
y = ["abc", "def", "ghi"]
z = ["ABC", "DEF", "GHI"]
a = ["abc", "def", "ghi", "jkl"]
print(x == y)
print(x == z)
print(x == a)

#Nesting in a list

a = [80, 90]
b = [10, 20, 30, a]
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[3][1])

#                                       Lambda expression 

# abcd = lambda x, (x: Any, y: Any)

abcd = lambda x, y: x**y
print(abcd(4, 3))

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
f = filter(lambda x: x % 3 == 0, l1)
l2 = list(f)
print(l2)
f = map(lambda i: i ** 2, l1)
l3 = list(f)
print(l3)

from functools import reduce
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# f = reduce(lambda x, y: x + y, l)
# print(f)

l = [1, 2, 3, 4, 5, 6, 7, 8]
f = reduce(lambda x, y: x if x > y else y, l)
print(f)

l = [1, 2, 3, 4, 5, 6, 7, 8]
f = reduce(lambda x, y: x if x < y else y, l)
print(f)

#More uses of functions `map` and `filter` 

#List comprehension 

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [x ** 2 for x in l1]
print(l2)

l3 = [x for x in l1 if x % 2 == 0]
print(l3)

#Ques: 

# s = range(1, 20, 3)
# for i in s:
#     print(i if i % 2 == 0)



#                                    TUPLES IN PYTHON


# Syntax of tuple

a = 10 # type - int
b = 20, # type - tuple

c = "Ram" # type - str
d = "Ram" # type - tuple

# Mathematical operator
# + operator

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t3 = t1 + t2
print(t3)

# Multiplication (*) operator

t2 = t1 * 3
print(t2)

# IMPORTANT METHODS and FUNCTIONS of tuple in python:
# 1. len() function
# 2. count() method
# 3. index() method
# 4. sorted() function

t = (40, 10, 30, 20)
t1 = sorted(t)
print(t)
print(t1) # By default, it will generate a list. 

t = (40, 10, 30, 20)
t1 = sorted(t, reverse = True)
print(t1)

# 5. min() and max() functions

t = (40, 10, 30, 20)
print(min(t))
print(max(t))

#                               TUPLE PACKING/UNPACKING:

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d #packing
d, c, b, a = t #unpacking

# TUPLE PACKING

'''
l = []
for x in range(3):
    roll = int(input("Enter the roll number: "))
    name = input("Enter the name of the user:" )
    email = input("Enter the email id of user: ")
    phone = input("Enter the phone number of the user: ")
    t = roll, name, email, phone # Tuple Packing
    l.append(t)
for r, n, e, p in l:
    print("%5d %-15s %-20s %10s"%(r,n,e,p))

    # %5d -> 5 bits of digits/integer
    # %
'''

#                                   TUPLE COMPREHENSION

t = (x ** 2 for x in range(1, 6))
print(tuple(t))
print(type(t)) # <class 'generator'>
for x in t:
    print(x)