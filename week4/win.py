#!/usr/bin/python
from tkinter import *
win = Tk()
win.title("Hello")

w = 700
h = 300

# width height x y
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()


####################################################################
canvas = Canvas(win, width=w, height=h)
canvas.pack()

####################################################################

x = int((ws/2)-(w/2))
y = int((hs/2)-(h/2))
win.geometry(f"{w}x{h}+{x}+{y}")

# Code to add widgets will go here...
win.mainloop()
