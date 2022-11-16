from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that takes 2 parameters and draws a single line
# Parameters: the x and y coordinates of the line's starting point
# The function shall draw a line from that point to the center of the canvas
# Fill the canvas with lines from the edges (every 20 px) to the center


def line(x, y):
    canvas.create_line(x, y, 150, 150, fill="red")


for x in range(0, 300, 20):
    for y in range(0, 300, 20):
        line(x, 0)
        line(0, y)
        line(x, 300)
        line(300, y)


root.mainloop()
