"""First try at designing a scene with Turtle, includes making snow with circle and randint and being able to make many trees using one, forest loop that manipulates coordinates."""


___author___ = "730309291"

from turtle import Turtle, colormode, done

# function for square base of tree


def tree_base(base: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Makes the brown sqaure base of the tree, the trunk."""
    base.begin_fill()
    base.pencolor("black")
    base.fillcolor("brown")

    base.penup()
    base.goto(x, y)
    base.pendown()

    i: int = 0
    while i < 4:
        base.forward(width)
        base.right(length)
        i = i + 1
    base.end_fill()


def tree_triangles(triangles: Turtle, x: float, y: float, width: float, length: float) -> None:
    """When called, makes triangles that will make an evergreen tree."""
    triangles.begin_fill()
    triangles.pencolor("black")
    triangles.fillcolor("green")

    triangles.penup()
    triangles.goto(x, y)
    triangles.pendown()

    triangles.speed(100)

    i: int = 0
    while i < 3:
        triangles.forward(width)
        triangles.left(length)
        i = i + 1
    triangles.end_fill()


def tree_star(star: Turtle, x: float, y: float, width: float, length: float) -> None:
    """When called, makes a yellow triangle at the top of three that is then manipulated using star_loops to make a fun star."""
    colormode(255)
    star.begin_fill()
    star.pencolor("black")
    star.fillcolor(251, 250, 85)

    star.penup()
    star.goto(x, y)
    star.pendown()

    star.speed(100)

    i: int = 0
    while i < 3:
        star.forward(width)
        star.left(length)
        i = i + 1
    star.end_fill()


def star_loop(starlines: Turtle, x: float, y: float, length: float) -> None:
    """When called, manipulates line tracing around a triangle to make a fun star."""
    colormode(255)
    starlines.begin_fill()
    starlines.pencolor("yellow")
    starlines.fillcolor(251, 250, 85)

    starlines.penup()
    starlines.goto(x, y)
    starlines.pendown()

    starlines.speed(100)
    starlines.hideturtle()

    side_length: float = 120
    i: int = 0
    starlines.pensize(5)
    while (i < 9):
        starlines.begin_fill()
        side_length = side_length * 0.97
        starlines.forward(length)
        starlines.left(side_length)
        starlines.end_fill()
        i = i + 1


def forest(forest: Turtle, a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float, j: float, k: float, q: float, m: float, n: float, o: float) -> None:
    """When called, draws as many trees as you'd like using the counter variable in main."""
    tortoise: Turtle = Turtle()
    tree_base(tortoise, o, b, c, e)
    tree_triangles(tortoise, a, h, g, d)
    tree_triangles(tortoise, a, j, g, d)
    tree_triangles(tortoise, a, k, g, d)
    tree_triangles(tortoise, a, q, g, d)
    tree_triangles(tortoise, a, m, g, d)
    tree_triangles(tortoise, a, n, g, d)
    tree_star(tortoise, f, d, c, d)
    star_loop(tortoise, f, d, c) 
    

def main() -> None:
    """The entrypoint of my scene."""
    tortoise: Turtle = Turtle()
    i: int = 0
    position: float = -100.0
    leaves: float = -130.0
    decor: float = -90.0
    while i < 3:
        forest(tortoise, leaves, -100, 70, 120, 90.0, decor, 150, -99.5, -70, -50.0, -20.0, 5.0, 25.0, position)
        position = position + 60
        leaves = leaves + 60 
        decor = decor + 60
        i = i + 1
    snowflake(tortoise)


def snowflake(snow: Turtle) -> None:
    """Finally, decorate your forest with beautiful, randomly placed circular snows using the index variable to decide the quantity."""
    from random import randint
    i: int = 0
    while i < 40:
        snow.penup()
        snow.pencolor("black")
        snow.fillcolor("white")
        snow.begin_fill()
        snow.goto(randint(-200, 200), randint(-200, 200))
        snow.pendown()
        snow.speed(100)
        snow.circle(5)
        snow.end_fill()
        i = i + 1
    done()


if __name__ == "__main__":
    main()
