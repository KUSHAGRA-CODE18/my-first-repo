'''
print("Hi")
Value = 110
print(Value)
print(type(Value))
Value = 99.99
print(Value)
print(type(Value))
Name = "raj"
print(Name)
print(type(Name))

'''

'''
a, b, c = 10, 20, 30
print(a, b, c)
print(b, c, a)
a, b, c = 10, 20 # {values must be same as variables}
print(a, b, c)

'''

'''
a = b = c = 10
print(a, b, c)
'''

'''
a = 20
print("first assigned value : ", a)
print(type(a))
a = "kushagra"
print("second assigned value : ", a)
print(type(a))

'''

# REPRESENTATION OF DOUBLE
#120 = 12e1
#1200 = 12e2
#0.12 = 12e(-2)


# BUILT-IN DATA TYPES IN PYTHON
# 1. NUMERIC TYPES(INT, FLOAT, COMPLEX)
# 2. Bool
# 3. None
# 4. Str
# 5. Bytes
# 6. Bytearray
# 7. Tuple
# 8. List
# 9. Range
# 10. Set


'''
a = 2e2
b = 2E2
c = 2e4
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

'''

'''
a = 3 + 5j
print(a)
print(type(a))
b = -3 - 5.5j
print(b)
print(type(b))
print(a+b)
print(type(a+b))
print(a+b)
print(type(a-b))
print(a+b)
print(type(a*b))
print(a+b)
print(type(a/b))
'''

'''
a = True
b = ""
print(a+b)
print(a+a)
print(a-b)
print(a*b)
print(a/b) #{NOT ALLOWED IN BOOLEAN OPERATER}
c = bool(b) #[WE CAN USE IT WITHOUT ARITHMETIC OPERATOR]
print(a + c * 2) #[WE CANNOT USE ARITHMETIC OPERATOR IF WE TAKE A BOLLEAN DATATYPE AS EMPTY STRING]

'''

'''
a = None
print(a)
print(type(a))

'''
#BYTE => SMALLEST UNIT TO STORE ANY DATA


# name1 = "Manmeet"
# name2 = "KUSHAGRA"
# address_line1 = '''Kalam COTTAGE 2,
# knowledge Park 3, 
# Greater Noida'''
# print(name1)
# print(name2)
# print(address_line1)

'''
x = [10, 20, 30, 40, 50]
y = bytes(x)
print(type(x))
print(type(y))
print(x[0])
w = x[0]
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
print(x[-5])

'''

'''
x = [10, 20, 30, 40, 50]
for i in x:
    print(i)

'''

'''
x = [10, 20, 30, 40, 50]
y = bytes(x)
print(y)
'''

'''
a = range(5)
print(a)
for i in a:
    print(i)
print("--")
b = range(1, 10)
for i in b:
    print(i)
print("--")
c = range(1, 7, 2)
for i in c:
    print(i)
print("--")
d = range(10, 0, -2)
for i in d:
    print(i)
print("--")
e = range(10, 2)
for i in e:
    print(i)

'''

'''
a = 50
print(type(a))
b = float(a)
print(type(b))

a = 50.7
print(type(a))
b = int(a)
print(b)
print(type(b))

'''

'''
val1 = "abcd" + str(34)
val2 = 12 + int("56")
print(val1)
print(val2)

'''

'''
a = 5
n = float(a)
print(n)
print(type(n))

a = 5.9
n = int(a)
print(n)
print(type(n))

'''

'''
a = 10
b = 20
c = (a if a<b else b) + 89
print(c)

a = 10
b = -3
c = 90
s = (a if a<c else c) if a<b else (b if b<c else c)
print(s)

w = 50
x = 89
y = 30
z = 40
m = (((w) if w<z else (z)) if w<y else ((y) if y<z else (z))) if w<x else (((x) if x<z else (z)) if x<y else ((y) if y<z else (z)))
print(m)

'''

'''
h = (12 and 5) + 4
print(h)

i = (0 and 0) 
print(i)

j = (0 and 6) + 9
print(j)

k = ("" and 5)
print(k)

l = (None and 8)
print(l)

h = (12 or 5) + 4
print(h)

j = (0 or 6) + 9
print(j)

k = ("" or 5)
print(k)

l = (None or 8)
print(l)

'''

'''
print(not 24)
print(not "")

'''

'''
a = 30
b = 40
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)

'''

'''
a = 10
print(-a)

'''

'''
text = "Welcome to python programming"
print("Welcome" in text)
print("welcome" in text)
print("hgvt" in text)
print("hari" not in text)

'''

'''
a = 10
b = 10
print(id(a))
print(id(b))

'''

'''
a = 10
b = 12
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

'''

        # ___       __       ___     __            __ ___ ___  __        __
        #  |  |\ | |__| |  |  |     |__ |  | |\ | |    |   |  |  | |\ | |__
        # _|_ | \| |    |__|  |     |   |__| | \| |__  |  _|_ |__| | \|  __|

'''
name = input("enter your name :")
print("Your name is :", name)

a = float(input("Enter the 1st no. :"))
b = float(input("Enter the 2nd no. :"))
c = a + b
print(c)

'''

        #  __       __           __            __ ___ ___  __        __
        # |__ \  / |__| |       |__ |  | |\ | |    |   |  |  | |\ | |__
        # |__  \/  |  | |__     |   |__| | \| |__  |  _|_ |__| | \|  __|


from sys import argv
a = eval(argv[1])