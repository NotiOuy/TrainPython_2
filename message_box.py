from tkinter import *
from tkinter import messagebox  # import messagebox library


def click():
    messagebox.showinfo(title='This is an info message box', message='You are a person')
    while(True):
        messagebox.showwarning(title='This is an info message box', message='You got a VIRUS!!!')


window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
