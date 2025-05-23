import random

import colorgram
import turtle as t

## THIS IS ONLY PREP STEP TO GET COLORS FROM THE image.jpg
# extract colors from image.jpg into list of tuples, eg: [(250, 25, 125), (147,45,98)]
# colors = colorgram.extract("image.jpg", 30)
#
# ## from doc: https://pypi.org/project/colorgram.py/
# # print(colors[0])
# # first_rgb = colors[0].rgb
# # print(type(first_rgb))
# # print(first_rgb)
# # r, g, b = first_rgb # unpacking again
# # print(r)
#
# color_list = []
# for color in colors:
#     r, g, b = color.rgb # unpacking again
#     # print(r, g, b)
#     tuple_of_colors = r, g, b
#     color_list.append(tuple_of_colors)

# print(color_list)



color_list_no_white = [(232, 241, 239), (1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41),
                       (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171),
                       (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77),
                       (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136),
                       (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7)]

# CHALLENGE:
# draw 10x10 rows of spots
# size of dot : 20 spaced by 50

timmy = t.Turtle()
timmy.shape("blank") # makes turtle invisible when moving
t.colormode(255)
timmy.pensize(20)
timmy.speed(0) # fastest

def line_of_dots(y_axis_offset):
    timmy.penup()
    timmy.setx(-200)
    timmy.sety(y_axis_offset)
    for _ in range(10):
        timmy.color(random.choice(color_list_no_white))
        timmy.dot(20)
        # timmy.pu() # NOT needed
        timmy.forward(50)
        # timmy.pendown() # Not needed


y_axis = -200
for _ in range(10):
    line_of_dots(y_axis)
    y_axis += 50

screen = t.Screen()
# # screen.bgcolor("yellow")
# screen.screensize(200, 200) # didnt change anything for me
# print(screen.screensize())
screen.exitonclick()


