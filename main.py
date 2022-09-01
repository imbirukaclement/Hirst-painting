# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(191, 166, 121), (142, 165, 189), (136, 94, 57), (63, 100, 135), (219, 207, 130), (13, 23, 55), (183, 149, 168), (144, 175, 154), (56, 22, 10), (172, 152, 50), (51, 13, 27), (74, 116, 85), (124, 80, 99), (12, 35, 20), (178, 185, 217), (30, 51, 120), (212, 179, 195), (171, 205, 185), (159, 106, 133), (101, 120, 171), (116, 32, 49), (95, 152, 110), (123, 36, 23), (30, 86, 61), (165, 202, 211), (172, 106, 94)]
tim.speed("fastest")
tim.penup()
#tim.pendown()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100
for dot_count in range(1,number_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(100)
    if dot_count % 7 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)
        tim.forward(700)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

