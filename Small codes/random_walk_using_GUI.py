"""Turtle GUI Random Walk Simulation Utility."""

import random
import turtle as t
from typing import List, Tuple

DIRECTIONS: List[int] = [0, 90, 180, 270]


def random_rgb_color() -> Tuple[int, int, int]:
    """Return a random RGB color tuple."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def perform_random_walk(tim: t.Turtle, steps: int = 200, step_length: int = 30) -> None:
    """Execute a randomized directional walk path with dynamic RGB pen colors."""
    for _ in range(steps):
        tim.color(random_rgb_color())
        tim.forward(step_length)
        tim.setheading(random.choice(DIRECTIONS))


def main() -> None:
    """Run random walk turtle GUI application."""
    tim = t.Turtle()
    t.colormode(255)
    tim.speed("fastest")
    tim.pensize(15)

    perform_random_walk(tim, steps=200)

    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
