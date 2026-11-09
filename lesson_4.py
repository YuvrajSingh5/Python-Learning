#Lesson 4: Conditional Statements in Python

#Excercise 1: Check whether number is positive, negative or zero

a=float(input("Enter a Number:  "))
if a>0:
    print("Positive Number")
elif a<0:
    print("Negative Number")
else:
    print("Zero")

#Excercise 2: Simple Login Verification

username= str(input("Enter Username:"))

if username == "admin":
    password=str(input("Enter password: "))
    
    if password =="python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

# Exercise 3: Grading System

marks=float(input("Enter Marks: "))

if marks <0 or marks>100:
    print("Invalid Marks")
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("Fail")
