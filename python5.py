'''#Ques1: WAP to check the no. is negative or positive

x = int(input("Enter the number: "))

if x < 0:
    print("The number is less than zero.")
else:
    print("The number is greater than zero.")


#Ques2: WAP whether the name entered with the username we have.

user_name = "rahul"
x = input("Enter the name: ")

if user_name == x.lower():
    print("The name is valid.")
else:
    print("The name is invalid.")


#Ques3: WAP to find the greater no. between entered two numbers.

x = int(input("Enter the First number."))
y = int(input("Enter the Second number."))

if x > y:
    print("Greater number is", x)
else:
    print("Greater number is", y)



#Ques: WAP to find the biggest number among three numbers.

x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))
z = int(input("Enter the 3rd number: "))

if x > y and x > z:
    print("Grester number is ", x)
elif y > z:
    print("Greater number is ", y)
else:
    print("Greater number is ", z)
'''