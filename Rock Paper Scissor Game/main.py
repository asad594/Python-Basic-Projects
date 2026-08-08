"""Rock Paper Scissors Terminal CLI Game.

Implements standard Rock Paper Scissors rules against a randomized computer move engine,
rendering ASCII hand gesture visuals and maintaining continuous session scores.
"""

import random
from typing import List

ROCK = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

GAME_IMAGES: List[str] = [ROCK, PAPER, SCISSORS]
CHOICE_NAMES: List[str] = ["Rock", "Paper", "Scissors"]


def play_round() -> int:
    """Play a single round of Rock Paper Scissors.

    Returns:
        1 for player win, -1 for player loss, 0 for tie.
    """
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        return 0

    if user_choice < 0 or user_choice >= 3:
        print("Invalid number entered! You must choose 0, 1, or 2.")
        return 0

    print(f"\nYou chose: {CHOICE_NAMES[user_choice]}")
    print(GAME_IMAGES[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {CHOICE_NAMES[computer_choice]}")
    print(GAME_IMAGES[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw! 🤝")
        return 0
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win! 🎉")
        return 1
    else:
        print("You lose! 😭")
        return -1


def main() -> None:
    """Run interactive Rock Paper Scissors session with score tracking."""
    print("Welcome to Rock Paper Scissors Arcade!")
    player_score = 0
    computer_score = 0

    while True:
        result = play_round()
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

        print(f"\nScore -> Player: {player_score} | Computer: {computer_score}")
        replay = input("\nPlay another round? Type 'y' or 'n': ").strip().lower()
        if replay != 'y':
            print("\nFinal Session Score:")
            print(f"Player: {player_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
