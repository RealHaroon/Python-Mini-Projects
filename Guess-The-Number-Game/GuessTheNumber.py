#? Guess The Number
import random
num=random.randint(1,10)
noOfGuesses=0
b=False
while not b :
    guess=int(input("Enter Your Guess : "))
    if(guess == num):
        print(f"{num} You Guessed right.")
        print(f"You Guessed in {noOfGuesses} Times ")
        b=True
    elif(guess >num):
        print("To High")
    elif(guess < num):
        print("To low")
    else:
        print("Wrong input")
    noOfGuesses+=1
