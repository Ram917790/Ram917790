import random

lowest_number = 1
Highest_number = 100
Number=random.randint(lowest_number,Highest_number)
guesses=0
running=True

#Here We running because if any in the program we can use the running=False so that we can get out of the loop
while running:
    guess=input("Guess a Number : ")

    if guess.isdigit():
        guesses +=1
        guess=int(guess)
        if guess < lowest_number or guess > Highest_number:
            print(f"Enter in the range of {lowest_number} & {Highest_number} only")
        if Number < guess:
            print(f'Your Guess {guess} is Higher Than Number')
        elif Number > guess:
            print(f'Your {guess} is lower than the number')
        else:
            print(f"You {guess} is Correct")
            print(f'CORRECT !--have been Guessed in {guesses} Guesses')
            break
    else:
        print("invalid")
        print(f"Enter in the range of {lowest_number} & {Highest_number} only")
print("Thank U for Playing The Guessing Game")