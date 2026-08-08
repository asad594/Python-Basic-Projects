"""Family Member Directory Loop Builder Utility."""

from typing import Dict


def build_family_dictionary(count: int) -> Dict[str, str]:
    """Collect family member names and relations via interactive prompts."""
    family: Dict[str, str] = {}
    for i in range(count):
        name = input(f"Enter name of family member #{i + 1}: ").strip()
        relation = input(f"Enter relation of {name}: ").strip()
        family[name] = relation
    return family


def main() -> None:
    """Run interactive family directory builder CLI."""
    try:
        n = int(input("How many family members do you want to add?: "))
        directory = build_family_dictionary(n)
        print("\n--- Family Directory Summary ---")
        for member, rel in directory.items():
            print(f"  {member}: {rel}")
    except ValueError:
        print("Invalid number input!")


if __name__ == "__main__":
    main()
