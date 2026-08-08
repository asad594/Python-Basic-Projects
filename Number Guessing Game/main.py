"""Number Guessing Terminal CLI Game.

Generates a random target number between 1 and 100, prompting the user for numeric
guesses with feedback ('Too High' / 'Too Low') and limited turns based on selected difficulty.
"""

import random

LOGO = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess: int, actual_answer: int, turns: int) -> int:
    """Compare user guess with target number and return remaining turn count.

    Args:
        user_guess: The integer guessed by player.
        actual_answer: Target random integer.
        turns: Remaining attempts count.

    Returns:
        Updated turn count.
    """
    if user_guess > actual_answer:
        print("Too High! 📈")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low! 📉")
        return turns - 1
    else:
        print(f"🎉 You got it! The answer was indeed {actual_answer}.")
        return turns


def set_difficulty() -> int:
    """Prompt player to select game difficulty ('easy' or 'hard')."""
    while True:
        choice = input("Choose difficulty level. Type 'easy' or 'hard': ").strip().lower()
        if choice == "easy":
            return EASY_LEVEL_TURNS
        elif choice == "hard":
            return HARD_LEVEL_TURNS
        print("Invalid choice! Please select 'easy' or 'hard'.")


def play_game() -> None:
    """Execute a single interactive session of the Number Guessing Game."""
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a target number between 1 and 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0

    while guess != answer and turns > 0:
        print(f"\nYou have {turns} turns remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print(f"\n❌ You ran out of turns! The target number was {answer}. You lose!")
        elif guess != answer:
            print("Guess again.")


if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nDo you want to play again? Type 'y' or 'n': ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break