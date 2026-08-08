"""Prime Number Verification Utility."""


def is_prime(num: int) -> bool:
    """Determine if an integer is a prime number.

    Args:
        num: Target integer.

    Returns:
        True if num is prime (>1 with no divisors other than 1 and itself), False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main() -> None:
    """Run interactive Prime Checker CLI."""
    try:
        number = int(input("Enter a number to check prime status: "))
        if is_prime(number):
            print(f"{number} is a Prime number.")
        else:
            print(f"{number} is NOT a Prime number.")
    except ValueError:
        print("Invalid number input!")


if __name__ == "__main__":
    main()