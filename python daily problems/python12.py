'''#                                   FUNCTIONS IN PYTHON:

# A function is a block of code that is used to perform a specific task.
# Terminology:
# - Function Definition: The block of code that defines what the function does.
# - Function Call: The act of using the function in the program.
# - Parameters: The variables defined in the function definition.
# - Arguments: The values passed to the function when it is called.


def my_function():
    print("Hello, World!")

my_function()

# if you did this, you will get an error because the function is called before it is defined. In Python, you must define a function before you can call it.

# my_function()
# def my_function():
#     print("Hello, World!")

#a function can take parameters, which are values that are passed to the function when it is called. These parameters can be used within the function to perform specific tasks.

def addnum(a, b):
    print("The sum of", a, "and", b, "is:", a + b)
    print("sum is %.2f" % (a + b))
    print("sum is {:.2f}".format(a + b))
    print(f"sum is {a + b:.2f}")
addnum(5, 10)
addnum(30.9, 20.1)

# Returning values from a function: 
# 
# A function can return a value using the return statement. The returned value can be used in the program where the function is called.

def sum(a, b):
    c = a + b
    return c

x = sum(10, 15)
print("Sum of two variables is: ", x)

def rn1():
    print("This function is returning nothing.")
    return

c = rn1()
print(c)

def rn2(a, b):
    c = a + b
    d = a - b
    return c, d

x, y = rn2(15, 10)
print("Sum is:", x)
print("Subtraction is:", y)



# ASSIGNING A FUNCTION TO A VARIABLE IN PYTHON

def add():
    print("We assigned function to variable.")

# Assign function to variable
sum = add
# calling function
sum()

def message(text):
    print(text)

def printmessage(x):
    x("Hello, World!")
printmessage(message)


def printmessage(x):
    x("Hello, World!")
printmessage(print)

'''
#functions a=can be passed to another function as an argument

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def process(func, x, y):
    return func(x, y)

print(process(add, 10, 10))
print(process(sub, 20, 10))

# function can be defined in another function

def outer():
    print("Outer Function!!")
    def inner():
        print("Inner Function!!")
    inner()
outer()

# A function can return another function

def outer():
    print("Outer Function!!")
    def inner():
        print("Inner Function!!")
    return inner
func = outer()
func()

def createfunction():
    def add(x, y):
        return x+y
    
    def sub(x, y):
        return x-y
    
    return add, sub

add_function, sub_function = createfunction()
print(add_function(10, 20))
print(sub_function(20, 10))

l = [add_function, 34, 78]
print(l[0](l[1], l[2]))

#             SUMMARY

# There are 4 properties of Functions
# - a function can be stored in a variable
# - a function can be passed to a function
# - a function can be defined inside a function
# - a function can be returned from a function



# Types of arguments in Python functions 

# 1. FORMAL ARGUMENTS:- Arguments used inside the function and used to do calculation.
#                     - are always values
# 2. ACTUAL aRGUMENTS:- Arguments given in function call
#                     - can be variable or values

def FUNC(a, b): # FORMAL ARGUMENTS
    c = a + b
    d = a - b
    return c, d

x, y = FUNC(15, 10) # ACTUAL ARGUMENTS
print(x, y)

# TYPES OF ARGUMENTS:

# 1. POSITIONAL ARGUMENTS:

def add(x, y):
    return x+y
print(add(10, 20))

# 2. KEYWORD ARGUMENTS:

def sub(x1, y1):
    return x1-y1
print(sub(x1 = 10, y1 = 20))
print(sub(y1 = 20, x1 = 10))

# 3. DEFAULT ARGUMENTS:

def simpleinterest(p, r = 2.5, t = 1):
    return (p*r*t)/100
print(simpleinterest(1000))
print(simpleinterest(1000, 3.5))
print(simpleinterest(1000, 3.5, 2))

# Variable length arguments

def sum(x, *y):
    for i in y:
        x+=i
    return x
print(sum(10, 20))
print(sum(10, 20, 30, 40, 50))
print(sum(10, 20, 30, 40, 50, 60, 70))
print(sum(10,))


def sum(*y):
    x=0
    for i in y:
        x+=i
    return x
print(sum(10, 20))
print(sum(10, 20, 30, 40, 50))
print(sum(10, 20, 30, 40, 50, 60, 70))
print(sum(10,))
print(sum())

# Keyword variable-length argument (for keyword argument). 

def printdata(**data): # "**" Before the data means, it is a dictionary and can take variable-length keyword argument. 
    print(type(data))
    for key, value in data.items():
        print(key, "=", value)

printdata(name = "Amit", age = 25, city = "Delhi")
printdata(id = 101, dept = "IT", salary = "9999", location = "Noida")
printdata(a=10, b=20, c=30, d=40, e=50, f=60)

