import turtle
kalem=turtle.Turtle()
kalem.color("red")
kalem.pensize(5)
kalem.speed(7)
for i in range (6):
    for j in range (6):
        kalem.forward(80)
        kalem.left(60)
    kalem.left(60)
turtle.done()