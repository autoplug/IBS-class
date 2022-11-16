#!/usr/bin/python
from tkinter import *


def print_myvar(m):
    print(m.get())


win = Tk()
win.title("Hello")

w = 700
h = 500

# width height x y
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()


####################################################################
canvas = Canvas(win, width=w, height=h)
canvas.pack()

my_line = canvas.create_line(100, 0, 300, 150, fill="red")
my_rec = canvas.create_rectangle(0, 0, 100, 100, fill="green")
canvas.create_text(400, 400, text="Hello", fill="red")

# Button definition
my_button = Button(win, text="close", width=20,
                   height=1, bd="1", command=win.destroy)
my_button.place(x=170, y=90)

# input
in_val = StringVar()
input_field = Entry(win, textvariable=in_val)
canvas.create_window(400, 10, window=input_field)
input_field.place(x=100, y=150)


# Checkbox
myvar = BooleanVar(name="myIntVar")
ckbox = Checkbutton(win, text="Yes or No", variable=myvar,
                    onvalue=True, offvalue=False, command=lambda: print_myvar(myvar))
ckbox.place(x=150, y=400)


# button to print value of checkbox
my_button2 = Button(win, text="print", width=20,
                    height=1, bd="1", command=lambda: in_val.set(str(myvar.get())))
my_button2.place(x=100, y=190)
####################################################################

x = int((ws/2)-(w/2))
y = int((hs/2)-(h/2))
win.geometry(f"{w}x{h}+{x}+{y}")

# Code to add widgets will go here...
win.mainloop()
