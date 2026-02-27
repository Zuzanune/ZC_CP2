#ZC 2nd CP2 fractal patern generator
from turtle import *
wn = Screen()
tracer(0)
wn.title("fractal patern generator")
turt = Turtle()
turt.shape("triangle")
pensize(2)
turt.teleport(-150, -150)
#ask user how many layers deep
deep = int(input("how many layers of triangle do you want to generate:  ").strip())
if deep == 0:
    deep = 5
#ask user for backround color. provide list
while True:
    bkcolor = input("what do you want the backround to be colored. enter a color available to the turle library. \n some common examples are Green, ivory, white, red, coral, maroon, and RoyalBlue. \n for a full list go to this link: https://cs111.wellesley.edu/reference/colors \n")
    if not bkcolor:
        bkcolor = "white"
    try:
        wn.bgcolor(bkcolor)
    except:
        print ("that is not a valid color")
        continue
    break

#define triangle making function
def triangle(type):
#if triangle recursions = user layers:
        #break   
    if type == deep:
        return "true"
    # distance = parameters distance
    else:
        inc = 2 ** (type - 1)
        #have turtle generate a set of triangles, 3 triangles. perfect. 60 degree turns, move 150 across screen.
        def draw_set():
            for i in range(3):
                for y in range(2):
                    turt.forward(100/inc)
                    if y == 0:
                        triangle(type + 1)
                turt.left(120)
            turt.end_fill()
        draw_set()
        # for the next triangle, call the function with distance/2 and start points halfway.
triangle(1)
hideturtle()
turt.hideturtle()
update()
done()