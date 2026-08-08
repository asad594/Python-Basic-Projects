"""Turtle GUI Square and Dashed Line Drawer Utility."""

import turtle as t


def draw_square(tim: t.Turtle, side_length: int = 120) -> None:
    """Draw a square using turtle graphics."""
    for _ in range(4):
        tim.forward(side_length)
        tim.right(90)


def draw_dashed_line(tim: t.Turtle, segments: int = 15, segment_len: int = 10) -> None:
    """Draw a dashed line segment using penup/pendown toggles."""
    for _ in range(segments):
        tim.forward(segment_len)
        tim.penup()
        tim.forward(segment_len)
        tim.pendown()


def main() -> None:
    """Run square and dashed line turtle GUI application."""
    turtles = t.Turtle()
    turtles.shape("classic")
    turtles.shapesize(2)
    draw_square(turtles, 120)

    tom = t.Turtle()
    tom.color("blue")
    draw_dashed_line(tom, 15, 10)

    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()