# a, b = 10, 20
# min = a if a < b else b
# print(min)

        # PYTHON LOOPS
        # 1. while loop
        # 2. for loop

#Ques: WAP to print the munbers from 1 to 5.

x = 1
while x <= 5:
    print(x)
    x += 1
print("End")


#Ques: WAP to print even numbers between 10 to 20 using while loop.

x = 10
while x <= 20:
    print(x)
    x += 2
print("End")


#Ques: WAP to print elements of list

x = [10, 20, 30, "Python"]
for i in x:
    print(i)
print("End")


#Ques: WAP to print charecters from string

x = "python"
for vh in x:
    print(vh)
print("End")


#Ques: WAP to print every item cost by adding gst

items_costs = [10, 20, 30]
gst = 2
for i in items_costs:
    print(i + gst)
print("End")


#Ques: WAP to print elements by using range() function and for loop.

for x in range(1, 5):
    print(x)
print("End")


#Ques: wap to print the sum of elements in the list

item_costs = [10, 20, 30]
sum = 0 #ACCUMULATION VARIABLE
for x in item_costs:
    sum += x
print(sum)
print("End")


#Ques: WAP to input a number and print the sum of digits
a = input("Enter the number: ")
if a.isdigit():
    sum = 0
    for i in a:
        sum += int(i)
    print("Sum of digits:", sum)
else:
    print("Enter only integer value!!")