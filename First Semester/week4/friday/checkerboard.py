from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

checker_width = 15
# Fill the canvas with a checkerboard pattern
bol = True
for x in range(0, 600, checker_width):
    for y in range(0, 600, checker_width):
        c = "black" if bol else "red"
        bol = not bol
        canvas.create_rectangle(
            x, y, x+checker_width, y+checker_width, fill=c)
    bol = not bol
root.mainloop()
