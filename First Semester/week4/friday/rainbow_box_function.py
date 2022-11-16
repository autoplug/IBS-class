from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a square drawing function that takes 2 parameters
# (the square size and the fill color)
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).


def rainbow(size, color="red"):
    canvas.create_rectangle(150-size, 150-size, 150+size, 150+size, fill=color)


colors = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")

for x in colors:
    rainbow(50, x)

root.mainloop()
