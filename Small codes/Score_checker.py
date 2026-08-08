"""Academic Subject Score Evaluation Utility."""


def evaluate_subject_scores(maths_score: float, english_score: float) -> str:
    """Classify academic performance across Maths and English scores.

    Args:
        maths_score: Mathematics score percentage.
        english_score: English score percentage.

    Returns:
        Evaluation summary string.
    """
    if maths_score >= 90 and english_score >= 90:
        return "You are good in both subjects."
    elif english_score >= 90:
        return "You are only good in English but not in Maths."
    elif maths_score >= 90:
        return "You are only good in Maths but not in English."
    else:
        return "You are neither good in English nor in Maths."


def main() -> None:
    """Run interactive Score Checker CLI."""
    try:
        maths = float(input("Enter Maths score: "))
        english = float(input("Enter English score: "))
        result = evaluate_subject_scores(maths, english)
        print(f"Evaluation: {result}")
    except ValueError:
        print("Invalid score input!")


if __name__ == "__main__":
    main()