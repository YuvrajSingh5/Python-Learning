# Lesson 3: Operators in Python

#Execercise 1: perform each arithmatic operation on the user input
a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))

print("Sum= ", a+b)
print("Sub= ", a-b)
print("Product= ", a*b)
print("Div Result= ", a/b)
print("FDiv Result= ", a//b)
print("Remainder= ", a%b)
print("Power= ", a**b)

#Exercise 2: Comparison Practice

age = int(input("Enter your age: "))

print(age >= 18)

# Excercise 3:Eligibility Checker

a= int(input("Enter your age: "))
Vid=input(("Do you have have a valid id? (Y/N): "))
Vid= Vid.lower()=="y"

if (a>=18 and a<=35 and Vid==True):
    print ("Eligible")
else: 
    print("not eligible")

#Excercise 4: Assignment Operators: Predict the output.
x = 10

x += 5
x *= 2
x -= 10
x //= 4

print(x)

# Final Excercise: Student Eligibility Checker

name= input("Enter Student's Name: ").strip()
age= int(input("Enter Student's Age: "))
eng= int(input("Enter English Marks:"))
maths= int(input("Enter Maths Marks:"))
science= int(input("Enter Science Marks:"))

total_marks= eng+maths+science
average_marks=total_marks/3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if(age>=18 and age<=25 and average_marks>=60 and name!=""):
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")