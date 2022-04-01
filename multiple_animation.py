from tkinter import *
import time
from Ball import *

window = Tk()

WIDTH = 700
HEIGHT = 700

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
tennis_ball = Ball(canvas, 0, 0, 40, 3, 6, "yellow")
basket_ball = Ball(canvas, 0, 0, 130, 8, 7, "green")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.0001)


window.mainloop()
