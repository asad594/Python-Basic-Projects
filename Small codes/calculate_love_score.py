"""Love Score Calculator Utility."""


def calculate_love_score(name1: str, name2: str) -> int:
    """Calculate compatibility score based on occurrence of letters in 'TRUE' and 'LOVE'.

    Args:
        name1: First name string.
        name2: Second name string.

    Returns:
        Two-digit combined integer score.
    """
    combined_names = (name1 + name2).lower()

    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")

    score_str = f"{true_count}{love_count}"
    return int(score_str)


def main() -> None:
    """Run interactive Love Score Calculator CLI."""
    print("Welcome to the Love Score Calculator!")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    score = calculate_love_score(name1, name2)
    print(f"Love Compatibility Score for {name1} & {name2}: {score}%")


if __name__ == "__main__":
    main()
