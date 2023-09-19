#flower
import turtle

turtle.speed(0)
turtle.setup(800,800)
turtle.width(2)
turtle.bgcolor("black")

colors = ["yellow", "orange"]
for j in range(50):
    for c in colors:
        turtle.color(c)
        for i in range(15):
            for c in colors:
                turtle.color(c)
                turtle.right(90)
                turtle.circle(200-j*4, 90)
                turtle.left(90)
                turtle.circle(200-j*4, 90)
                turtle.right(180)
                turtle.circle(50,24)
                turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()