from tkinter import *

win = Tk()
canvas = Canvas(win, width='300', height='300')
canvas.pack()

line = canvas.create_line(150, 0, 150, 150, fill="green")
line = canvas.create_line(0, 150, 150, 150, fill="red")

win.mainloop()
