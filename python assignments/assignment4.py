'''Ques. Write a python program to perform the following string
 slicing operations on the given string "PYTHONPROGRAMMING'''

string = "PYTHONPROGRAMMING"
#1.
A = string[0:3]

#2.
B = string[14:]

#3.
C = string[2:8]

#4.
D = string[0::2]

#5.
E = string[18::-1]

print(A)
print(B)
print(C)
print(D)
print(E)

'''
Ques. Write a python program that takes your name and convert it into password.

WHAT TO DO:
1. Take the input
2. Separate it into 3 different sub-string
3. reverse every sub-string 
4. concatenate them all

Eg: Kushagra --> uKgashar
'''

Name = input("Enter your name: ")
l = len(Name)
first = Name[1::-1]
print("first: ",first)
mid = Name[-3:1:-1]
print("mid: ", mid)
last = Name[:-3:-1]
print("last: ",last)
password = first + mid + last
print(password)