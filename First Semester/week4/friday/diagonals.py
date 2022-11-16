from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def diagonal(x1, y1, x2, y2):
    if x1 == 0:
        canvas.create_line(x1, y1, x2, y2, fill="green")
    else:
        canvas.create_line(x1, y1, x2, y2, fill="red")
    return


diagonal(0, 0, 300, 300)
diagonal(300, 0, 0, 300)
root.mainloop()
