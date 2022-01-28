import turtle
import random

# turtle config
t = turtle.Turtle()
s = turtle.Screen()
t.speed(100)
t.pencolor("#ffffff")
s.bgcolor("#000000")


if __name__ == "__main__":
    magic = 9
    try:
        for _ in range(500):
            r = random.randrange(-10, 10)
            a = r * random.choices(range(10 * magic, 100))[0]
            b = a - random.choices(range(10 * magic, 100))[0]
            bb = a / random.choices(range(10 * magic, 100))[0]
            y = [a, random.choices([b, bb])[0]]
            x = random.choices(y)
            y.remove(x[0])
            t.pencolor(str("#{0:06x}".format(random.randrange(0x1, 0xFFFFFF))))
            t.setpos(x[0], y[0])

    except Exception as e:
        print("WARNING", "Exit!")
