"""Blackjack (Black Jackson) Terminal Card Game.

Implements classic Blackjack card game logic against an automated dealer AI,
handling aces (11 vs 1), blackjacks (21 with 2 cards), and dealer hits under 17.
"""

import random
from typing import List

LOGO = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/                 
"""


def deal_card() -> int:
    """Return a random card value from a standard Blackjack deck representation."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards: List[int]) -> int:
    """Calculate hand total score, converting Ace (11) to 1 if score exceeds 21.

    Returns:
        0 if the hand is a Blackjack (2 cards totaling 21), otherwise total score.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    cards_copy = list(cards)
    while 11 in cards_copy and sum(cards_copy) > 21:
        cards_copy.remove(11)
        cards_copy.append(1)

    return sum(cards_copy)


def compare(user_score: int, computer_score: int) -> str:
    """Compare final user and computer scores to determine match result string."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif user_score == 0:
        return "Win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win! 😁"
    elif user_score > computer_score:
        return "You win! 😃"
    else:
        return "You lose 😤"


def play_game() -> None:
    """Execute a single interactive round of Blackjack."""
    print(LOGO)
    user_cards: List[int] = []
    computer_cards: List[int] = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer AI loop: hit while total score is less than 17
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


if __name__ == "__main__":
    while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        play_game()