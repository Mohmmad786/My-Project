from turtle import *
tracer(10)
setposition(0, 20)
bgcolor("black") 
colors = ["red","blue","purple","green"]
hideturtle ()
for i in range(360):
    for c in colors:
        color(c)
        circle(170) #-i ,100
        left(60)
        circle(170)
        right(50)
done()