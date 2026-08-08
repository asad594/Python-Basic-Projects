"""FizzBuzz Evaluation Utility."""


def evaluate_fizz_buzz(number: int) -> str:
    """Return 'FizzBuzz', 'Fizz', 'Buzz', or string of number.

    Args:
        number: Target integer.

    Returns:
        String classification of FizzBuzz rules.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def main() -> None:
    """Run interactive FizzBuzz CLI."""
    try:
        num = int(input("Enter a number to evaluate FizzBuzz status: "))
        print(f"Result: {evaluate_fizz_buzz(num)}")
    except ValueError:
        print("Invalid integer input!")


if __name__ == "__main__":
    main()
