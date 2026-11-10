# #Lesson 4: Conditional Statements in Python

#Excercise 1: Check whether number is positive, negative or zero

a=float(input("Enter a Number:  "))
if a>0:
    print("Positive Number")
elif a<0:
    print("Negative Number")
else:
    print("Zero")

# #Excercise 2: Simple Login Verification

username= str(input("Enter Username:"))

if username == "admin":
    password=str(input("Enter password: "))
    
    if password =="python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

# # Exercise 3: Grading System

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

#Lesson 4: Part 2:

#Exercise 4: Movie Ticket Booking System

customer_age= int(input("Enter your age: "))
has_id= str(input("Do you have an id? (y/n) "))
has_id= has_id.lower()=="y"
if customer_age>=18:
    if has_id:
        print("Ticket Booking Allowed")
    else:
        print("Ticket Booking Denied")
else:
    print("Ticket Booking Denied")

Exercise 5: Employee Bonus Calculator

salary= float(input("Enter your Salary:  "))
experience= float(input("Enter your experience(in years):  "))
rating= float(input("Enter your performance rating: "))

if salary < 0 or experience < 0 or rating < 0 or rating > 10:
    print("Invalid input")
elif salary>=25000 and rating>=7 and experience>=2:
    print("Eligible for Bonus")
else:
    print("Not eligible for bonus")

# Exercise 6: ATM Withdrawal:

account_balance=float(input("Enter your account balance: "))
if account_balance < 0:
    print("Invalid Account Balance")
else:
    withdrawal_amount=float(input("How much do you want to withdraw? "))
    if withdrawal_amount<=0:
        print("Invalid Amount")
    elif withdrawal_amount>account_balance:
        print("Insufficient Funds")
    else:
        print(f"Remaining Balance : {account_balance-withdrawal_amount}")

#Exercise 7:Mini ATM Menu
print("Choose an option \n 1. Check Balance \n 2. Deposit Money \n 3. Withdraw Money\n"  )
i= (int(input("Select Your option:  ")))
balance=84500

if i==1:
    print(f"Your Current Balance is:{balance}")
elif i==2:
    deposit_amount= (float(input("Enter the amount:")))
    if deposit_amount<=0:
        print("Invalid Amount")
    else:
        balance=balance+deposit_amount
        print(f"Amount Successfully Deposited. Current Balance:{balance+deposit_amount}")
elif i==3:
    withdraw_amount=float(input("Enter Amount to be Withdrawn: "))

    if withdraw_amount>balance:
        print("Insufficent Funds")
    elif withdraw_amount<=0:
        print("Invalid Amount")
    else:
        print("Withdraw Successful")
        balance=balance-withdraw_amount
        print(f"Remaining Balance:{balance}")
else:
    print("Invalid Option")

#Exercise 8: Student Result Calculator

name= str(input("Enter Student's Name: ")).strip()
maths= float(input("Enter Math Marks: "))
if maths< 0 or maths>100:
    print("Invalid Marks")
else:
 science= float(input("Enter Science Marks: "))
 if science<0 or science>100:
    print("Invalid Marks") 
 else:
  english= float(input("Enter English Marks: "))
  if english<0 or english>100:
    print("Invalid Marks")
  else:
     history= float(input("Enter History Marks: "))
     if history<0 or history>100:
       print("Invalid Marks")
     else:
      geography= float(input("Enter Geography Marks: "))
      if geography<0 or geography>100:
        print("Invalid Marks")
      else:
        total_marks= maths+science+english+history+geography
        percantage= float(total_marks/5)

        print(f"Total marks: {total_marks}/500 & Percentage: {percantage}%")
        if percantage>=90 and percantage<=100:
          print("Student's Grade : Grade A")
        elif percantage>=75 and percantage<=89.99:
          print("Student's Grade : Grade B")
        elif percantage>=60 and percantage<=74.99:
          print("Student's Grade : Grade C")
        elif percantage>=40 and percantage<=59.99:
          print("Student's Grade : Grade D")
        else:
          print("Fail")

