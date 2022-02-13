from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.begin_fill()
leo.pencolor("pink")
leo.fillcolor(171, 239, 254)

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.speed(25)
leo.hideturtle()

i: int = 0 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.pencolor("black")

bob.up()
bob.goto(45, 60)
bob.down()

bob.speed(75)

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1


i: int = 0
while (i < 23):
    side_length == side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i = i + 1

done()