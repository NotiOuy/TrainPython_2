from tkinter import *


def submit():
    print(f"You have ordered: {listbox.get(listbox.curselection())}")


window = Tk()

listbox = Listbox(window,
                  font=("Time New Roman", 40))
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Potato")
listbox.insert(3, "Pasta")
listbox.insert(4, "Tomato")

listbox.config(height=listbox.size())

submitButton = Button(window, text="Please click on me!", command=submit)
submitButton.pack()

window.mainloop()
