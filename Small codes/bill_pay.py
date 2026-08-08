"""Bill Pay Roulette Utility."""

import random
from typing import List


def pick_random_payer(friends_list: List[str]) -> str:
    """Select a random friend from the list to pay the bill."""
    if not friends_list:
        raise ValueError("Friends list cannot be empty.")
    return random.choice(friends_list)


def main() -> None:
    """Run interactive Bill Pay Roulette CLI."""
    friends = ["Asad", "Abdullah", "Rayyan", "Amanullah", "Umair", "Maazuddin"]
    payer = pick_random_payer(friends)
    print(f"🎉 {payer} will pay the bill today!")


if __name__ == "__main__":
    main()
