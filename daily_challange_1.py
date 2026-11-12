# Challange 1: Ask a user to enter a positive interger n.
# Print:
# The sum of all even numbers from 1 to n.
# The sum of all odd numbers from 1 to n.
# Total count of numbers divisible by 3.

n=int(input("Enter a positive integer: "))
etotal=0
ototal=0
count=0

if n<=0:
    print("Invalid Input.")
else:
         for i in range(2,n+1,2):
          etotal=etotal+i
         print(f"Sum of Even Numbers: {etotal}")

         for j in range(1,n+1,2):
          ototal=ototal+j
         print(f"Sum of Odd Numbers: {ototal}")

         for k in range(3,n+1,3):
          if k%3==0:
           count+=1
         print(f"Count of numbers divisible by 3: {count}")  

# Challenge 3: Problem-Solving – Number Guessing Game
# Improve your previous guessing game.

# Requirements:
# - Set a secret number.
# - Give the user a maximum of 5 attempts.
# - Print "Too High" or "Too Low" after each incorrect guess.
# - If the user guesses correctly, display a success message and stop.
# - If all attempts are exhausted, reveal the secret number.    

secret_number = 7

for i in range(1, 6):
    print(f"Attempt {i} of 5")
    num = int(input("Enter your guess: "))
    if num == secret_number:
        print("Congratulations! Correct Answer.")
        break
    elif num < secret_number:
        print("Too Low! Try again.")
    else:
        print("Too High! Try again.")
else:
    print(f"Sorry! The secret number was {secret_number}.")
