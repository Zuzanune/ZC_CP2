#ZC 2nd CP2 fractal patern generator
from turtle import *
from helper import triangle

#ask user how many layers deep

#ask user for backround color. provide list
while True:
    wn = Screen()
    tracer(0)
    wn.title("fractal patern generator")
    turt = Turtle()
    turt.shape("triangle")
    pensize(2)
    turt.teleport(-150, -150)
    deep = int(input("how many layers of triangle do you want to generate:  ").strip())
    if deep == 0:
        deep = 5
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
    while True:
        colr = input("what would you like the color of the fractal to be. enter a color available to the turtle library \n")
        if not colr:
            colr = "black"
        try:
            turt.pencolor(colr)
        except:
            print ("that is not a valid color")
            continue
        break

    triangle(1, deep, colr)
    hideturtle()
    turt.hideturtle()
    update()
    while True:
        print ("would you like to generate another fractal? (y/n)")
        ag = input()
        if ag not in ["Y","N", "y", "n"]:
            print("that is not a valid answer")
            continue
        break
    if ag == "Y" or ag == "y":
        continue
    else:
        print ("goodbye")
        done()
        break
    