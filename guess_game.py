import random

jackpot=random.randint(1,100)

counter=1

print("Welcome to the Number Guessing Game!")

print("Try to guess the number between 1 and 100.")

number=int(input("Enter the input From the user: "))

while number!=jackpot:

    if number<jackpot:

        print("Wrong Guess! please Guess Higher")
    else:

        print("Wrong Guess! please Guess Lower")

    number=int(input("Enter the input: "))
    
    counter+=1

else:
    print("Correct Guess")

    print("Your Guess are : ")

    print("Your attempt is: ",counter)

