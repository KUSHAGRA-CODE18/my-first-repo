#Ques. give the input: "ABCDEF PYTHON STRING"
#      get the output: "ACE PTO SRN"

St = 'ABCDEF PYTHON STRING'
Str = ""
l = St.split()
for i in range(len(l)):
    sl = l[i][0::2]
    Str += sl + " "
print(Str)
