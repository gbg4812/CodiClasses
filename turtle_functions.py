import turtle as t


def star(size):
    t.width(size / 10)
    t.setheading(0)

    t.color("gold")
    t.begin_fill()

    t.left(36)
    for i in range(5):
        t.forward(size)
        t.left(180 - 36)

    t.end_fill()
    t.color("black")


def snowflake(res, size):
    width = size / 10
    t.color("skyblue")
    t.width(width)

    i = 0
    while i < 6:
        t.left(60)
        snow_fractal(res, size, width)
        i += 1


def snow_fractal(res, size, width):
    t.width(width)
    if res <= 0:
        return
    i = 0
    while i < 3:
        t.forward(size / 3)
        t.right(60)
        snow_fractal(res - 1, size / (2 + i), width / 2)
        t.width(width)
        t.left(120)
        snow_fractal(res - 1, size / (2 + i), width / 2)
        t.width(width)
        t.right(60)
        i += 1

    t.up()
    t.back(size)
    t.down()
