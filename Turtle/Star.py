import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.color("black")

for i in range(5):
    t.right(144)
    t.forward(200)

window.exitonclick()