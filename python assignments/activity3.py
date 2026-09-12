#Ques. Write a python programme to count repeated charecter in a string

str = "thequickbrownfoxjumpsoverthelazydog"
stu = ""
for i in str:
    if i in stu:
        continue
    else:
        a = str.count(i)
        if a > 1:
            print("Occurence of",i,"is: ",a)
        stu = stu + i
