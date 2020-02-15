from turtle import mainloop, Turtle, Screen

RIGHT_ANGLE = 90
SPEED = TIMES = 1000
WIDTH = 1

YELLOW = "#FFA500"
BLUE = "#00BFFF"
BLACK = "black"


def rose(pen: Turtle, length_line=0) -> None:
    """recursive function that generate a quadractic rose

    Arguments:
        pen {Turtle}

    Keyword Arguments:
        length_line {int} -- [description] (default: {0})
    """

    if length_line < TIMES:
        if(length_line % 2 == 0):
            pen.pencolor(BLUE)
        else:
            pen.pencolor(YELLOW)
        pen.forward(length_line)
        pen.left(RIGHT_ANGLE + 1)
        rose(pen, length_line + 3)


if __name__ == "__main__":

    pen = Turtle()
    canvas = Screen()

    pen.screen.bgcolor(BLACK)
    pen.width(WIDTH)
    pen.speed(SPEED)

    try:
        rose(pen)
        canvas.exitonclick()

    except Exception as e:
        print("WARNING", "Exit!")
