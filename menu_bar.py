from tkinter import *


def openFile():
    print("File has been opened!")


def saveFile():
    print("File has been saved!")


def quite():
    exit(window)


def cut():
    print("You cut some text!")


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

optionMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=optionMenu)
optionMenu.add_command(label="Open", command=openFile)
optionMenu.add_command(label="Save", command=saveFile)
optionMenu.add_separator()
optionMenu.add_command(label="Exit", command=quite)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)

window.mainloop()
