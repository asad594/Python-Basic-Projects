"""Safe Input Exception Handling Utility."""


def get_integer_input(prompt: str) -> int:
    """Prompt user for an integer until valid input is received, handling ValueError safely."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric integer value.")


def odd_or_even(number: int) -> str:
    """Determine if integer is odd or even."""
    return "This is an even number." if number % 2 == 0 else "This is an odd number."


def main() -> None:
    """Run exception handling demonstration CLI."""
    num = get_integer_input("Enter a number to evaluate: ")
    print(odd_or_even(num))


if __name__ == "__main__":
    main()