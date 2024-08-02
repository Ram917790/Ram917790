import random


number = random.randint(1,20)
Guesses = 0
#here we are starting loop
while True:
    guess=int(input("Enter A Number You Guess : "))
    Guesses += 1
    #we have been used the 0 and adding the guesses
    if number < guess:
        print(f"Guess {guess} Number is High")
    elif number > guess:
        print(f"Guess {guess} Number is Low")
    else:
        print("Your Guess Correct")
        break
print(f"You Have Been Guessed in {Guesses} guesses")



