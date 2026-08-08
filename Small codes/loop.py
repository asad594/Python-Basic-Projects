"""Iteration & Loop Traversal Demonstration Utility."""

from typing import List


def print_fruits_iteration(fruits: List[str]) -> None:
    """Iterate through list of fruits and print formatted text."""
    print("--- FRUITS ITERATION ---")
    for fruit in fruits:
        print(f"Fruit: {fruit} | Dessert: {fruit} Pie")


def print_states_iteration(states: List[str]) -> None:
    """Iterate through US states list."""
    print("\n--- US STATES ITERATION ---")
    for index, state in enumerate(states, 1):
        print(f"{index:02d}. {state}")


def main() -> None:
    """Run loop iteration demonstrations."""
    fruits = ["Apple", "Peach", "Pear"]
    print_fruits_iteration(fruits)

    states_of_america = [
        "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
        "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
        "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
        "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
        "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
        "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
        "New Mexico", "Arizona", "Alaska", "Hawaii"
    ]
    print_states_iteration(states_of_america)


if __name__ == "__main__":
    main()