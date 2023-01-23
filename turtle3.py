from turtle import *
color("blue", "light blue")
pensize(5)
speed(10)
begin_fill()
while True:
    forward(200)
    left(250)
    if abs(pos()) < 1:
        break
end_fill()
done()