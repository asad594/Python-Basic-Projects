"""Automatic Password Generator Module.

Provides functions to generate customizable, secure random passwords with mixed characters,
symbols, and numbers.
"""

import random
from typing import List

LETTERS: List[str] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS: List[str] = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(num_letters: int, num_symbols: int, num_numbers: int) -> str:
    """Generate a randomized password string based on specified component counts.

    Args:
        num_letters: Count of alphabetic characters.
        num_symbols: Count of special symbols.
        num_numbers: Count of numeric digits.

    Returns:
        A shuffled string containing specified elements.
    """
    char_list: List[str] = []
    char_list.extend(random.choice(LETTERS) for _ in range(max(0, num_letters)))
    char_list.extend(random.choice(SYMBOLS) for _ in range(max(0, num_symbols)))
    char_list.extend(random.choice(NUMBERS) for _ in range(max(0, num_numbers)))

    random.shuffle(char_list)
    return "".join(char_list)


def main() -> None:
    """Interactive CLI runner for PyPassword Generator."""
    print("Welcome to the PyPassword Generator!")
    try:
        no_of_letters = int(input("How many letters would you like in your password?\n"))
        no_of_symbols = int(input("How many symbols would you like?\n"))
        no_of_numbers = int(input("How many numbers would you like?\n"))
    except ValueError:
        print("Invalid input! Please enter positive integer values.")
        return

    result = generate_password(no_of_letters, no_of_symbols, no_of_numbers)
    print(f"\nThe final generated password is: {result}")


if __name__ == "__main__":
    main()
