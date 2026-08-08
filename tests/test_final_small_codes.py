"""Unit tests for final batch of Small codes utilities."""

import sys
from pathlib import Path

# Add Small codes directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "Small codes"))

from Score_checker import evaluate_subject_scores
from buy_alcohole import can_buy_alcohol
from roller_coaster import check_roller_coaster_eligibility
from printing_table_using_func import generate_multiplication_table
from table import generate_reverse_table


def test_evaluate_subject_scores():
    assert evaluate_subject_scores(95, 92) == "You are good in both subjects."
    assert evaluate_subject_scores(80, 95) == "You are only good in English but not in Maths."
    assert evaluate_subject_scores(92, 85) == "You are only good in Maths but not in English."
    assert evaluate_subject_scores(70, 75) == "You are neither good in English nor in Maths."


def test_can_buy_alcohol():
    assert can_buy_alcohol(20) is True
    assert can_buy_alcohol(18) is True
    assert can_buy_alcohol(17) is False


def test_check_roller_coaster_eligibility():
    assert check_roller_coaster_eligibility(130, 80) is True
    assert check_roller_coaster_eligibility(115, 80) is False
    assert check_roller_coaster_eligibility(130, 110) is False


def test_generate_multiplication_table():
    table = generate_multiplication_table(5, 3)
    assert len(table) == 3
    assert table[0] == (5, 1, 5)
    assert table[2] == (5, 3, 15)


def test_generate_reverse_table():
    rev_table = generate_reverse_table(4, 5)
    assert len(rev_table) == 5
    assert rev_table[0] == (4, 5, 20)
    assert rev_table[-1] == (4, 1, 4)
