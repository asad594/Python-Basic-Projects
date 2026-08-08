"""Dictionary-Based Calculator CLI Application.

Executes arithmetic operations by mapping math operator strings to python functions
in a dictionary dispatch table, supporting continuous accumulation calculations.
"""

from typing import Callable, Dict

LOGO = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1: float, n2: float) -> float:
    """Return sum of n1 and n2."""
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    """Return difference of n1 and n2."""
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    """Return product of n1 and n2."""
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    """Return division of n1 by n2, handling zero division."""
    if n2 == 0:
        raise ValueError("Division by zero is undefined.")
    return n1 / n2


OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def get_number(prompt: str) -> float:
    """Prompt user for a numeric input until a valid float is provided."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculator() -> None:
    """Execute continuous dictionary calculator interactive loop."""
    print(LOGO)
    should_continue = True
    num1 = get_number("Enter the first number: ")

    while should_continue:
        print("\nAvailable Operations:")
        for symbol in OPERATIONS:
            print(f"  {symbol}")

        op_symbol = input("Pick an operation: ").strip()
        if op_symbol not in OPERATIONS:
            print("Invalid operation selected!")
            continue

        num2 = get_number("Enter the next number: ")

        try:
            calculation_function = OPERATIONS[op_symbol]
            answer = calculation_function(num1, num2)
            print(f"\nResult: {num1} {op_symbol} {num2} = {answer}")
        except ValueError as err:
            print(f"Math Error: {err}")
            continue

        choice = input(
            f"\nType 'y' to continue calculating with {answer}, 'n' to start new calculation, or 't' to terminate: "
        ).strip().lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Thank you for using the Python Dictionary Calculator! Goodbye.")


if __name__ == "__main__":
    calculator()
