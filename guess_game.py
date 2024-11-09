import random

jackpot=random.randint(1,100)

counter=1
number=int(input("Enter the number: "))

while number!=jackpot:
    if number<jackpot:

        print("Wrong Guess! please Guess Higher")
    else:

        print("Wrong Guess! please Guess Lower")

    number=int(input("Enter the input: "))
    
    counter+=1

else:
    print("Correct Guess")
    print("Your attempt is: ",counter)

