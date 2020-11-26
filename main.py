# Colorgram
# import colorgram

# Extracting 6 colors from image.jpg
# colors = colorgram.extract("image.jpg", 30)

# Creating an empty list to add the extracted colored in:
# rgb_colors = list()
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

from turtle import Turtle, Screen
from random import  choice

color_list = [
    (202, 164, 109), (150, 75, 49), (223, 201, 135), (52, 93, 124),
    (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
    (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164),
    (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
    (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

timmy = Turtle()
screen = Screen()
screen.colormode(255)


timmy.speed(5)

# timmy starting position:
timmy.penup()
timmy.back(200)
timmy.right(90)
timmy.forward(300)
timmy.left(90)
timmy.pendown()

def hirst_painting():
    for i in range(100):
        timmy.dot(20, choice(color_list))

        timmy.penup()
        timmy.forward(50)

        timmy.pendown()
        if timmy.xcor() > 220:
            timmy.left(90)
        if timmy.xcor() < -180:
            timmy.right(90)
        timmy.hideturtle()


hirst_painting()


screen.exitonclick()