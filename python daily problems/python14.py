# def factorial(n):
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n - 1)
#     return result
# x = factorial(4)
# print("Factorial of 4 is:", x)

# #                       LAMBDA FUNCTIONS

# # with the help of def:
# def cube(x):
#     return x*x*x
# l = [1, 2, 3, 4, 5]
# l1 = list(map(cube, l))
# print(l1)

# #with the help of lamda function
# l2 = list(map(lambda x:x*x*x, l))
# print(l2)

# num = list(map(int, input().split()))
# print(num)

# def cube(x):
#     return x*x*x
# num = list(map(cube, [int(i) for i in input().split()]))
# print(num)

# num1 = [cube(x) for x in [int(i) for i in input().split()]]
# print(num1)

# num2 = list(map(cube, list(map(int, input().split()))))
# print(num2)

# # generator function

# def abcd(func, l):
#     for i in l:
#         yield func(i)
# l = [1, 2, 3, 4]
# l2 = list(abcd(cube, l))
# print(l2)


# def genval(start, end, step):
#     while (start <= end):
#         yield start
#         start+=step
# print(list(genval(0, 12, 2)))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = list(filter(lambda x: x > 6, l))
# print(l1)

# from functools import reduce
# l = ["Python", "is", "a", "programming", "language"]
# longest_word = reduce(lambda x, y: x if len(x)>len(y) else y, l)
# print(longest_word)
# print(len(longest_word))


#                        Exception Handling

"""
print("one")
print("two")
try:
    print(10/0)
except ZeroDivisionError:
    print("exception passed")
print("four")

"""
"""
try:
    print(10/0)
except ZeroDivisionError as z:
    print("Exception information.", z)

"""
"""
try:
    x = int(input("Enter the 1st number:"))
    y = int(input("Enter the 2nd number:"))
    print(x/y)
except ZeroDivisionError:
    print("Can't devide by zero")
except ValueError:
    print("Please provide integer value only")

"""
"""
try:
    x = int(input("Enter the 1st number:"))
    y = int(input("Enter the 2nd number:"))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print("Please provide numbers only and problem is:", e)
"""

"""
try:
    x = int(input("Enter the 1st number:"))
    y = int(input("Enter the 2nd number:"))
except ZeroDivisionError:
    print("Can't devide by zero")
except ValueError:
    print("Please provide integer value only")
except:
    print("Defualt error: please provide valid input only!!")
"""

'''
try:
    print("try block")
except:
    print("Except block")
finally:
    print("Finally block")
'''

"""
try:
    print("try block")
    print(10/0)
except ZeroDivisionError:
    print("Except block")
finally:
    print("Finally block")
"""

"""
try:
    print("try block")
    print(10/0)
except NameError:
    print("except block")
finally:
    print("Finally block")
"""