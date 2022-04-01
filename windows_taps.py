from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays

tab1 = Frame(notebook)      # new frame for tab1
tab2 = Frame(notebook)      # new frame for tab2

notebook.add(tab1,
             text="TAB_1")
notebook.add(tab2,
             text="TAB_2")
notebook.pack(expand=True, fill="both")      # expend = expend to fill any space not otherwise

Label(tab1,
      text="Hello, this is tab#1",
      width=50,
      height=25).pack()
Label(tab1,
      text="Hello, this is tab#2",
      width=50,
      height=25).pack()

window.mainloop()
