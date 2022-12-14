import random as rand
#Number Guessing Game Objectives:
EASY = 10
HARD = 5
# Include an ASCII art logo.
from test import art
print("Welcome to the number guessing game!\n")

print(art)
# Allow the player to submit a guess for a number between 1 and 100.
# print("Think of a number between 1-100\n")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



def level():
    difficulty = str(input("Choose a difficulty. Type 'easy' or'hard': \n"))
    if difficulty == "easy":
        return EASY
    elif difficulty == "hard":
        return HARD
    else:
        print("No valid difficulty was selected!\n")

computer_number = rand.randint(1,100)

def guess(computer_number):
    i=0
    attempts = level()
    while i < attempts:
        print(f"You have {attempts} attempts remaining")
        user_guess = int(input("Make a guess: "))
        attempts -= 1
        if attempts>0:
            if computer_number > user_guess:
                print("Too Low.\nGuess Again.\n")
            elif computer_number < user_guess:
                print("Too High.\nGuess Again.\n")
            else:
                print(f"You got it! The answer was {computer_number}")
                break
        else:
            print(f"\nWrong! You have {attempts} attempts remaining!\nGame Over!")

guess(computer_number)
