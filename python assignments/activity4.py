#Ques;

eng = int(input("Enter the marks of English: "))
hindi = int(input("Enter the marks of Hindi/Telugu: "))
maths = int(input("Enter the marks of Maths: "))
sci = int(input("Enter the marks of Science: "))
geo = int(input("Enter the marks of Geography: "))
his = int(input("Enter the marks of History: "))

avg = (eng + hindi + maths + sci + geo + his)/6
print("Average marks of Ramu is ", "%.0f"%avg) # %.0f -> no decimal places
                                               # %.1f -> upto one decimal places
                                               # %.2f -> upto two decimal places



if avg <= 100 and avg >=90:
    print("Grade = A+")

elif avg <= 89 and avg >=80:
    print("Grade = A")

elif avg <= 79 and avg >=70:
    print("Grade = B+")

elif avg <= 69 and avg >=60:
    print("Grade = B")

elif avg <= 59 and avg >=45:
    print("Grade = C")

elif avg <= 44 and avg >=33:
    print("Grade = D")

elif avg <= 32 and avg >=0:
    print("Fail")

else:
    print("Invalide input to find the grades")

print("Ultimately")

if  avg >= 33 and avg <= 100:
    print("RANU IS PASSED")
else:
    print("RAMU IS FAILED")