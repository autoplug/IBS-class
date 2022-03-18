from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that takes 1 parameter and draws one square
# Parameter: the square size
# The function shall draw a square of that size to the center of the canvas
# Draw at least 3 squares with that function.
# (the squares should not be filled otherwise they will hide each other)
# Avoid code duplication!


def center_box(size):
    canvas.create_rectangle(150-size, 150-size, 150+size, 150+size)


center_box(70)
center_box(50)
center_box(30)

root.mainloop()
