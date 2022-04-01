# grid() = geometry manager that organizes widgets in a tabel-like structure in a parameters

from tkinter import *

window = Tk()

Label(window,
      text="First name:",
      font=("Time New Roman", 20)).grid(row=0, column=0)
Entry(window).grid(row=0, column=1)

Label(window,
      text="Last name:",
      font=("Time New Roman", 20)).grid(row=1, column=0)
Entry(window).grid(row=1, column=1)

window.mainloop()