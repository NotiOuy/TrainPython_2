# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *


def submit():
    my_text = text.get("1.0", END)
    print(my_text, end="")


window = Tk()

text = Text(window, font=("Ink Free", 14),
            padx=20,
            pady=20,
            height=10,
            width=25,
            bg="light yellow")
text.pack()

button = Button(window, font=("Ink Free", 14), text="submit", command=submit)
button.pack()

window.mainloop()






