# #                               DICTIONARIES IN PYTHON

# d = {}
# d[1] = "Arun"
# d[2] = "Chetan"
# d[1] = "Kushagra"
# print(d)

# # Accessing dictionaries in Python 

# d = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}
# print(d[1])
# print(d[2])
# print(d[3])

# # print(d[4]) # KeyError: It occurs when the key is not available in the given dictionary. 

# if 400 in d:
#     print(d[400])
# else:
#     print("Key not found")


# # Ques:

# d = {}
# n = int(input("Enter the number of employees: "))
# i = 1
# while i <= n:
#     name = input("Enter the name of the employee: ")
#     salary = input("Enter the salary of the employee: ")
#     d[name] = salary
#     i +=1
# for x in d:
#     print("The name is: ", x, "and his salary is:", d[x])


# del keyword

d = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}
print("Before deleting a key from a dictionary ", d)
del d[1]
print("After deleting a key from dictionary: ", d)

# del() function

e = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}
print("Before deleting a key from a dictionary: ", e)
del(e[2])
print("After deleting a key from a dictionary: ", e)

#                           Creating a dictionary

# 1. dict() function

d = dict()
print(d)
print(type(d)) # Creating an empty dictionary 


d = dict({1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"})
print(d)

# .get() method

d = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}

print(d.get(1))
print(d.get(100))

print("----------------------------------------------------")

print(d.get(1))
print(d.get(100, "No key found")) # We give a default value, so we cannot get `None`. 

# .pop() method

d = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}
print("Before pop: ", d)
d.pop(1)
print("After pop: ", d)

# .popitem() method

d = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}
print("Before popitem: ", d)
d.popitem()
print("After popitem: ", d) # It will pick a random key and pop it. Doesn't follow any order 
                            # it will give a key error if the dictionary is empty


# items() method

d = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}
for k, v in d.items():
    print(k, "---", v)

# copy() method

d1 = {1 : "Ramesh", 2 : "Suresh", 3 : "Mahesh"}

#                                  Dictionary comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
d = {i : i ** 2 for i in l1}
l2 = [i ** 2 for i in l1]
t = (i ** 2 for i in l1)
t = tuple(t)
print("Dictionary comprehension: ", d)
print("List comprehension: ", l2)
print("Tuple Comprehension: ", t)