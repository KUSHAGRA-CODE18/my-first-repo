                                    # LOOPS IN PYTHON

                        #1. OUTER LOOP: x [generate number] [per line]
                        #2. INNER LOOP: Y [executer x times] [works x times in same time]



# Eg:

# 1.
# *
# **
# ***
# ****
# *****

for x in range(1,6):
    for y in range(x):
        print("*", end="")
    print()


# 2.
# *
# ***
# *****
# *******

for x in range(1,8,2):
    for y in range(x):
        print("*", end="")
    print()


# 3.
# 1
# 22
# 333
# 4444
# 55555

for x in range(1,6):
    for y in range(x):
        print(x, end="")
    print()


# 4.
# 1
# 12
# 123
# 1234
# 12345

for x in range(1,6):
    for y in range(1,x+1):
        print(y, end="")
    print()


#5.

for x in range(1,6):
    for y in range(x):
        print(x+y, end="")
    print()


# 6.
# # * # * #
# # * # *
# # * #
# # *
# #

for x in range(5,0,-1):
    for y in range(x):
        if y%2 != 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
print("--------------------------------------")

                                    #BREAK IN PYTHON

'''             The BREAK element when encountered will terminate the loop 
                        and bring the execution out of the loop.''' 

group = [1, 2, 3, 4]
search = int(input("Enter the number you want to search: "))
for element in group:
    if element == search:
        print("Element found in the group")
        break;
print("--------------------------------------")


                                    #CONTINUE IN PYTHON

'''             The CONTINUE element when encountered will skip that value in the loop 
                            and execute the rest of the loop.''' 

for x in range(1,500):
    if x % 10 == 0:
        continue;
    print(x)
print("--------------------------------------")

#Ques: WAP to print the item which are below 500 in the give list.

cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        continue;
    print("items", item)
print("--------------------------------------")

for x in range(1,500):
    if x % 10 == 0 or x % 5 == 0:
        pass;
    else:
        print(x)
print("--------------------------------------")

# while-else loop

x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print("Invalid")
print("--------------------------------------")

x = 1
while x <= 10:
    print(x)
    x += 1
    if x == 2:
        break;
else:
    print("Invalid")
print("--------------------------------------")

# for-else loop

for x in [1, 2, 3, 4, 5]:
    print(x)
else:
    print("Completed")
print("--------------------------------------")

for x in [1, 2, 3, 4, 5]:
    print(x)
    if x == 3:
        break;
else:
    print("Completed")
print("--------------------------------------")

group = [1, 2, 3, 4]
search = int(input("Enter the number you want to search: "))
for elements in group:
    if search == elements:
        print("Element found - Search completed")
        break;
else:
    print("Element not found")