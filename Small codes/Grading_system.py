"""Student Grading System Utility."""

from typing import Dict


def calculate_grade(score: int) -> str:
    """Convert numeric score to grade category string."""
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Fail"


def convert_scores_to_grades(scores: Dict[str, int]) -> Dict[str, str]:
    """Map student dictionary of scores to grade classifications."""
    return {name: calculate_grade(score) for name, score in scores.items()}


def main() -> None:
    """Display sample student grades."""
    student_scores = {
        'Harry': 88,
        'Ron': 78,
        'Hermione': 95,
        'Draco': 75,
        'Neville': 60
    }
    grades = convert_scores_to_grades(student_scores)
    print("Student Grades Summary:")
    for student, grade in grades.items():
        print(f"  {student}: {grade}")


if __name__ == "__main__":
    main()
