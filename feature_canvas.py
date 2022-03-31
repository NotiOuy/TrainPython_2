# canvas = widget that is used to draw graph, plots, image in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
canvas.create_line(0, 0, 500, 300, fill="Red", width=5)
canvas.create_line(0, 500, 500, 0, fill="Blue", width=5)
canvas.create_rectangle(50, 120, 200, 70, fill="purple")
canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="yellow", outline="black", width=5)
canvas.pack()

window.mainloop()
