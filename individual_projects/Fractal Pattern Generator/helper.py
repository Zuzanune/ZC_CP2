from turtle import *
#define triangle making function
def triangle(type, deep, color):
#if triangle recursions = user layers:
        #break
    pencolor(color)
    if type == deep:
        return "true"
    
    # distance = parameters distance
    else:
        inc = 2 ** (type - 1)
        #have turtle generate a set of triangles, 3 triangles. perfect. 60 degree turns, move 150 across screen.
        def draw_set():
            for i in range(3):
                for y in range(2):
                    forward(100/inc)
                    if y == 0:
                        triangle(type + 1, deep, color)
                left(120)
            end_fill()
        draw_set()
        # for the next triangle, call the function with distance/2 and start points halfway.