from turtle import *
pensize(2)
speed(360)
color("purple")
for i in range(36):
     forward(100)
     backward(100)
     left(10)
color("red")
setpos(100,100)
for i in range(36):
     forward(100)
     backward(100)
     left(10)
color("green")
goto(-100,100)
for i in range(36):
     forward(100)
     backward(100)
     left(10)
color("blue")
goto(-100,-100)
for i in range(36):
     forward(100)
     backward(100)
     left(10)
color("dark orange")
goto(100,-100)
for i in range(36):
     forward(100)
     backward(100)
     left(10)
done()