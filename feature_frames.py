# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window)
frame.pack()

Button(frame,
       text="W",
       font=("Console", 25),
       width=3,
       relief=RAISED,
       bd=5).pack(side=TOP)
Button(frame, text="A",
       font=("Console", 25),
       width=3,
       relief=RAISED,
       bd=5).pack(side=LEFT)
Button(frame,
       text="S",
       font=("Console", 25),
       width=3,
       relief=RAISED,
       bd=5).pack(side=LEFT)
Button(frame,
       text="D",
       font=("Console", 25),
       width=3,
       relief=RAISED,
       bd=5).pack(side=LEFT)

window.mainloop()





