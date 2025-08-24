# Number-guessing-game-
import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def checking_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too High")
        return turns-1
    elif user_guess<actual_answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it!.The answer is {actual_answer}")

def set_difficulty():
    choice=input("Choose the difficulty level ? Type 'easy' or 'hard' : ").lower()
    if choice=="easy":
        return EASY_LEVEL_TURNS
    elif choice=="hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input")

def game():
    print("Welcome to the number guessing game ")
    print("I am thinking of a number between 1 and 100")
    answer=random.randint(1,100)
    print(f"PSST. The correct answer is {answer}")
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} turns remaining utlize in best way and win the game ")
        guess=int(input("Make a guess  : "))
        turns=checking_answer(guess,answer,turns)
        if turns==0:
            print("You ran out of turns! .You loose")
        elif guess!=answer:
            print("Guess Again")

game()