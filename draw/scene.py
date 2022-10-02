# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from tkinter import W
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    w0=0
    w1=100
    diameter = 50
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas,scene_width, scene_height)
    draw_ground(canvas,scene_width)
    draw_clouds(canvas,diameter,w0,w1)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)



# Draw functions
def draw_sky(canvas, width,height):
    draw_rectangle(canvas, 0, 0, width, height, outline="blue",fill='midnightblue')

def draw_ground(canvas,width):
    draw_rectangle(canvas,0,0,width,150,fill='chartreuse4')
def draw_garden(canvas):
    draw_rectangle(canvas,)
def draw_clouds(canvas,diameter,w0,w1):
    for z in range(4):
        for i in range(50):
            h=random.randint(350,400)
            w=random.randint(w0,w1)
            draw_oval(canvas,w,h,w+diameter,h+diameter, outline='white',fill='white')
        w0+=200
        w1+=200

# Call the main function so that
# this program will start executing.
main()