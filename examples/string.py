# str = "i am STUDYING python from Apnacollage"
# print(str.capitalize())
# print(str)

marks = int(input("enter your marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):    
    grade = "C"
else:
    grade = "D"
    print("your grade is:", grade)