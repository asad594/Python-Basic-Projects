"""Built-in Min, Max, and Sum Operations Utility."""

from typing import List, Tuple


def get_score_statistics_builtin(scores: List[int]) -> Tuple[int, int, int]:
    """Return total sum, minimum score, and maximum score using Python built-ins.

    Args:
        scores: List of integer scores.

    Returns:
        Tuple of (total_sum, min_score, max_score).
    """
    if not scores:
        raise ValueError("Scores list cannot be empty.")
    return sum(scores), min(scores), max(scores)


def main() -> None:
    """Run built-in statistics demonstration."""
    student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
    total, minimum, maximum = get_score_statistics_builtin(student_scores)
    print("--- Built-in Score Statistics ---")
    print(f"Total Sum : {total}")
    print(f"Minimum   : {minimum}")
    print(f"Maximum   : {maximum}")


if __name__ == "__main__":
    main()
