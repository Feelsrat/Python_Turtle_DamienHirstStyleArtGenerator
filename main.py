import random
import colorgram
import turtle as t

amount_of_colours_extracted = 10  # how many colours to extract from image.jpg
number_of_dots = 400  # total amount of dots in the image. This will affect how tall the image will be
spacing_between_dots = 25  # space between dots both vert and horiz

rgb_colors = []
colors = colorgram.extract('image.jpg', amount_of_colours_extracted)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

turtle = t.Turtle()
turtle.hideturtle()
t.colormode(255)
turtle.penup()
turtle.speed(0)
turtle.setheading(225)
turtle.forward(350)
turtle.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(spacing_between_dots)

    if dot_count % 20 == 0:
        turtle.setheading(90)
        turtle.forward(spacing_between_dots)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()
