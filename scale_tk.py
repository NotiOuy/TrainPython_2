from tkinter import *


window = Tk()

scale = Scale(window,
              from_=0, to=100,
              orient=HORIZONTAL,
              font=("Console", 30),
              resolution=10,
              tickinterval=5,
              length=1000
              )
scale.pack()

window.mainloop()