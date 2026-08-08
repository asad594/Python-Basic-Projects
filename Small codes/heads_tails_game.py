"""Heads or Tails Coin Flip Simulator Utility."""

import random


def flip_coin() -> str:
    """Simulate a coin flip and return 'Heads' or 'Tails'."""
    return "Heads" if random.randint(0, 1) == 0 else "Tails"


def main() -> None:
    """Run interactive Coin Flip CLI."""
    print("Welcome to the Heads and Tails Coin Flipper!")
    result = flip_coin()
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
