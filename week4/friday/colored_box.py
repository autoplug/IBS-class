from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x1 = 10
y1 = 30

x2 = 30
y2 = 70

canvas.create_line(x1, y1, x1, y2, fill="green")
canvas.create_line(x1, y1, x2, y1, fill="red")
canvas.create_line(x2, y1, x2, y2, fill="black")
canvas.create_line(x1, y2, x2, y2, fill="red")

root.mainloop()
