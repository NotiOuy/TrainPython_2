from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="*Path to file*")
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()
