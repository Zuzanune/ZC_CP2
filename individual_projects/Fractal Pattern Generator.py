#ZC 2nd CP2 fractal patern generator
from turtle import *
wn = Screen()
wn.title("fractal patern generator")
turt = Turtle()
#ask user how many layers deep
deep = int(input("how many layers of triangle do you want to generate:  ").strip())
#ask user for backround color. provide list
bkcolor = input("what do you want the backround to be colored. enter a color available to the turle library. \n some common examples are Green, ivory, white, red, coral, maroon, and RoyalBlue \n")
wn.bgcolor(bkcolor)

def triangle(type):
    if type == deep:
        return deep
    else:
        """inc = 2 ** (type - 1)"""
        for i in range(3):
            for y in range(2):
                turt.forward(150/deep)
                if y == 0:
                    triangle(type + 1)
            turt.left(120)
        turt.end_fill()
        
#define triangle making function with parameters distance
    #if triangle recursions = user layers:
        #break
    # distance = parameters distance
    #have turtle generate triangle. perfect. 60 degree turns, move 150 across screen. 
    # for the next triangle, call the function with distance/2 and start points halfway.
