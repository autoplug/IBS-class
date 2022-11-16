from tkinter import *
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


def center_line(x, y):
    canvas.create_line(x, y, 150, 150, fill="red")


center_line(0, 0)
center_line(200, 300)
center_line(0, 100)

root.mainloop()
