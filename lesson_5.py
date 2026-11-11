# Lesson 5: Loops in Python

# #Exercise 1: Print 1 to 10 using while loop
i=1
while i<=10:
  print(i)
  i=i+1

#Exercise 2: Countdown Timer
i=10
while i>=1:
  print(i)
  i=i-1
print("Happy New Year!!!")

#Exercise 3: Sum of Natural Numbers
i=1
total=0
while i<=10:
 total+= i
 i+=1
print(f"Sum:{total}")

#Exercise 4: Multiplication Table
n=int(input("Enter a number:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1

#Exercise 5: Stop at a Specific Number
i=1
while i<=10:
    if i==7:
        break
    print(i)
    i+=1

#Exercise 6: Write a program that prints numbers from 1 to 20 but skips all even numbers.
i=0
while i<20:
    i+=1
    if i%2==0:
        continue
    print(i)

#Exercise 7: Number Guessing Game
secret_num=7
while True:
    a=int(input("Guess the number:"))
    if a==secret_num:
     print("Congratulation! Correct Answer.")
     break
    else:
       print("Wrong Answer! Try Again.")

#Exercise 8: Improve the Number Guessing Game
secret_num=7
while True:
    a=int(input("Guess the number:"))
    if a==secret_num:
     print("Congratulation! Correct Answer.")
     break
    elif a<secret_num:
       print("Too Low! Try again.")
    else:
       print("Too High! Try Again.")

#Exercise 9:Write a program that prints numbers from 1 to 20 using a for loop.
for i in range(1,21):
    print(i)

#Exercise 10: Print all even numbers from 2 to 20 using a for loop.
for i in range(2,21,2):
    print(i)

#Exercise 11: Print the multiplication table of a number entered by the user, using a for loop.
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")

#Exercise 12: Write a program that asks the user for a number and calculates the sum of all numbers from 1 up to that number.
num=int(input("Enter a number:"))
total=0
for i in range(1,num+1):
    total+=i
print(f"Sum:{total}")

#Exercise 13: Write a program that calculates the factorial of a number entered by the user.
num=int(input("Enter a number:"))
total=1
for i in range(num,0,-1):
    total=total*i
print(f"Factorial of {num} is {total}")

#Exercise 14: Count the digits of a number using a while loop.
num= int(input("Enter an integer: "))
num= abs(num)
count=0
if num==0:
    count=1
else:
    while num>0:
        num=num//10
        count+=1
print(f"Number of digits: {count}")

#Exercise 15:  Reverse a number

num=int(input("Enter a number:"))
num=abs(num)
reverse=0
if num==0:
    reverse=0
else:
    while num>0:
        reverse= reverse*10 + num%10
        num=num//10
      
print(f"Reverse Number:{reverse}")

#Excercise 16: Palindrome Number
num=int(input("Enter a Number:"))
if num<0:
    sign=-1
else:
    sign=1

temp=abs(num)
reverse=0


while temp>0:
        reverse=reverse*10+temp%10
        temp=temp//10
reverse=reverse*sign

if num==reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")

#Exercise 17: Prime Number
num= int(input("Enter a number: "))
count=1
if num<=1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2,num+1,1):
        if num%i==0:
            count+=1
    if count==2:
        print(f"{num} is Prime.")
    else:
         print(f"{num} is not Prime.")

#Exercise 18: Fibonacci Series
num=int(input("How many terms you want? :"))
a=0
b=1
if num<=0:
    print("Plese enter a postive integer.")
else:    
    print("Fibonacci Series:")
    for i in range (0,num):
     print (a, end=" ")
     a,b=b,a+b

#Exercise 19: Number Pattern
num=1
for i in range(2,7):
    print(num)
    num=num*10+i    

#Exercise 20:
n=int(input("Enter a number: "))
if n<=0:
    print("Invalid input.")
else:
 for i in range(1,n+1,):
    for j in range(1,i+1):
        print(i, end=" ")
    print()
          



