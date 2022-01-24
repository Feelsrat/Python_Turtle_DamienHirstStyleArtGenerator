import random
import colorgram
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 6)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
turtle = t.Turtle()
t.colormode(255)
turtle.penup()
turtle.speed(0)
turtle.setheading(225)
turtle.forward(350)
turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

turtle.hideturtle()
screen = t.Screen()
screen.exitonclick()