from tkinter import *

win = Tk()
canvas = Canvas(win, width='300', height='300')
canvas.pack()

# Create a function that takes 2 parameters and draws one square
# Parameters: the x and y coordinates of the square's top left corner
# The function shall draw a 50x50 square from that point
# Draw 3 squares with that function
# Avoid code duplication!


def square(x, y):
    line = canvas.create_rectangle(x, y, x+50, y+50, fill="green")


square(0, 0)
square(40, 30)

win.mainloop()
