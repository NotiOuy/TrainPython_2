from tkinter import *


def move_up(event):
    canvas.move(myImage, 0, -10)


def move_down(event):
    canvas.move(myImage, 0, 10)


def move_right(event):
    canvas.move(myImage, 10, 0)


def move_left(event):
    canvas.move(myImage, -10, 0)


window = Tk()

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

canvas = Canvas(window, width=1250, height=700)
canvas.pack()

photoImage = PhotoImage(file="sports-car-b-5d21a240b70e103d1c72f7584f34699c94540e938f3104cb943c2ee134c0a779.png")
myImage = canvas.create_image(0, 0, image=photoImage, anchor=NW)

window.mainloop()