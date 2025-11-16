from turtle import*
import colorsys 
tracer(45)
bgcolor("black")

h = 0

for i in range(330):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    h +=0.0025
                # 150, 180, 360
    
    backward(150-i)
    right(150)
    backward(150-i)
    left(150)
    right(180/5)
    end_fill()
    # right(5,90)
hideturtle()
    
    
done()