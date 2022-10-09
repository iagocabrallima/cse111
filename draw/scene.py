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
    draw_lake(canvas,diameter)
    draw_fish1(canvas)
    draw_fish2(canvas)
    draw_fish3(canvas)
    draw_trees(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)



# Draw functions
def draw_sky(canvas, width,height):
    draw_rectangle(canvas, 0, 0, width, height, outline="blue", fill='midnightblue')

def draw_ground(canvas,width):
    draw_rectangle(canvas,0,0,width,150, fill='chartreuse4')
def draw_garden(canvas):
    draw_rectangle(canvas,)
def draw_clouds(canvas,diameter,w0,w1):
    for z in range(4):
        for i in range(50):
            h=random.randint(350,400)
            w=random.randint(w0,w1)
            draw_oval(canvas,w,h,w+diameter,h+diameter, outline='white', fill='white')
        w0+=200
        w1+=200
def draw_lake(canvas,diameter):
    for l in range(300):
        h=random.randint(0,100)
        w=random.randint(100,500)
        draw_oval(canvas,w,h,w+diameter,h+diameter, outline="blue", fill="blue")

def draw_fish1(canvas):
    draw_oval(canvas,120,35,170,45,outline="gray", fill="gray")
    draw_polygon(canvas,168,40,174,45,174,35,outline='gray', fill='gray')

def draw_fish2(canvas):
    draw_oval(canvas,300,45,350,55,outline="orange", fill="orange")
    draw_polygon(canvas,350,50,356,55,356,45,outline='orange', fill='orange')

def draw_fish3(canvas):
    draw_oval(canvas,400,45,450,55,outline="orange", fill="orange")
    draw_polygon(canvas,450,50,456,55,456,45,outline='orange', fill='orange')

def draw_trees(canvas):
    draw_rectangle(canvas, 600, 70, 620, 120, fill="brown")
    draw_polygon(canvas, 540, 110, 610, 320, 680, 110, fill="forestGreen")

    draw_rectangle(canvas, 700, 60, 720, 110, fill="brown")
    draw_polygon(canvas, 640, 100, 710, 310, 780, 100, fill="forestGreen")

# Call the main function so that
# this program will start executing.
main()