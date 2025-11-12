from turtle import *
tracer(250)
setposition(0, 25)
bgcolor("black") 
colors = ["red","blue","purple","green"]
hideturtle ()
for i in range(400):
    for c in colors:
        color(c)
        circle(175-i, 100)
        left(90)
        circle(175-i, 100)
        right(80)
done()