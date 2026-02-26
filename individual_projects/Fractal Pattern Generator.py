#ZC 2nd CP2 fractal patern generator
from turtle import *
import time
wn = Screen()
tracer(0)
wn.title("fractal patern generator")
turt = Turtle()
pensize(2)
#ask user how many layers deep
deep = int(input("how many layers of triangle do you want to generate:  ").strip())
#ask user for backround color. provide list
bkcolor = input("what do you want the backround to be colored. enter a color available to the turle library. \n some common examples are Green, ivory, white, red, coral, maroon, and RoyalBlue. \n for a full list go to this link: https://cs111.wellesley.edu/reference/colors \n")
if not bkcolor:
    bkcolor = "white"
wn.bgcolor(bkcolor)
#define triangle making function
def triangle(type):
#if triangle recursions = user layers:
        #break   
    if type == deep:
        return deep
    # distance = parameters distance
    else:
        inc = 2 ** (type - 1)
        #have turtle generate triangle. perfect. 60 degree turns, move 150 across screen.
        for i in range(3):
            for y in range(2):
                turt.forward(150/inc)
                if y == 0:
                    triangle(type + 1)
            turt.left(120)
        turt.end_fill()
        # for the next triangle, call the function with distance/2 and start points halfway.
triangle(1)
update()
done()