"""Turtle GUI Geometric Shapes Drawer Utility."""

import random
import turtle as t
from typing import List

COLORS: List[str] = [
    "blue", "dark green", "dark red", "orange",
    "firebrick", "purple", "hot pink", "indian red"
]


def draw_polygon(tim: t.Turtle, sides: int, side_length: int = 100) -> None:
    """Draw a regular polygon with a specified number of sides."""
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(side_length)
        tim.right(angle)


def main() -> None:
    """Run geometric shape drawing turtle application."""
    tim = t.Turtle()
    tim.speed("fast")

    for sides in range(3, 11):
        tim.color(random.choice(COLORS))
        draw_polygon(tim, sides)

    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
