from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)


window = Tk()
window.geometry("420x420")

button = Button(text='click', command=click)
button.pack()

window.mainloop()


