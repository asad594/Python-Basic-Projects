"""Interactive Turtle Etch-a-Sketch GUI Utility."""

import turtle as t

TIM = t.Turtle(shape="turtle")


def move_forwards() -> None:
    """Move turtle forward by 10 units."""
    TIM.forward(10)


def move_backwards() -> None:
    """Move turtle backward by 10 units."""
    TIM.backward(10)


def turn_left() -> None:
    """Turn turtle counter-clockwise by 10 degrees."""
    TIM.left(10)


def turn_right() -> None:
    """Turn turtle clockwise by 10 degrees."""
    TIM.right(10)


def clear_screen() -> None:
    """Clear canvas drawing and reset turtle home position."""
    TIM.clear()
    TIM.penup()
    TIM.home()
    TIM.pendown()


def main() -> None:
    """Run interactive Etch-a-Sketch controls GUI."""
    screen = t.Screen()
    screen.listen()

    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_screen, "c")

    print("Etch-A-Sketch Controls Active:")
    print("  W: Move Forward | S: Move Backward | A: Turn Left | D: Turn Right | C: Clear Canvas")

    screen.exitonclick()


if __name__ == "__main__":
    main()