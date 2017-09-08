import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")
t.color("green")

for i in range(4):
    t.forward(100)
    t.left(90)

t.fill()

t.penup()
t.goto(-200, 0)

t.pendown()

window.exitonclick()
