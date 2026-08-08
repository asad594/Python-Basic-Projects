"""Legal Age Eligibility Verification Utility."""


def can_buy_alcohol(age: int, legal_age: int = 18) -> bool:
    """Check if age meets or exceeds legal age threshold.

    Args:
        age: Person's age in years.
        legal_age: Legal threshold age (default 18).

    Returns:
        True if eligible, False otherwise.
    """
    return age >= legal_age


def main() -> None:
    """Run interactive Age Eligibility CLI."""
    try:
        age = int(input("Enter your age: "))
        if can_buy_alcohol(age):
            print("Eligible to buy alcohol.")
        else:
            print("Not eligible to buy alcohol.")
    except ValueError:
        print("Invalid age input!")


if __name__ == "__main__":
    main()
