"""Turtle GUI Spirograph Art Generator Utility."""

import random
import turtle as t
from typing import Tuple


def random_rgb_color() -> Tuple[int, int, int]:
    """Generate a random RGB color tuple."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_spirograph(tim: t.Turtle, gap_size: int = 5, radius: int = 100) -> None:
    """Draw a spirograph circular pattern using turtle graphics."""
    for _ in range(int(360 / gap_size)):
        tim.color(random_rgb_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + gap_size)


def main() -> None:
    """Run interactive Spirograph generator GUI."""
    tim = t.Turtle()
    t.colormode(255)
    tim.speed("fastest")

    draw_spirograph(tim, gap_size=5, radius=80)

    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
