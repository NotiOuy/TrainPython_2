# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets
# label = an area widget that hold text and/or an image within a window

from tkinter import *

window = Tk()  # instantiate an instance of a window
# window.geometry("720x400")
window.title("My first window")

icon = PhotoImage(file="lotos_icon_128.png")
window.iconphoto(True, icon)
window.config(background="White")


# photo = PhotoImage(file='download.jpg')

# label = Label(window,
#             fg='green',
#             bg='green',
#              padx=20,
#             compound='button',
#              relief=RAISED)
# label.pack()
# label.place(x=0, y=0)


def click():
    second_window = Tk()
    label = Label(second_window,
                  text="You clicked the button!!!")
    label.pack()
    second_window.mainloop()


button = Button(window,
                text="click me!!!",
                command=click,
                font=("Comic Sans", 40),
                activeforeground="#00FF00",
                activebackground="White",
                state=ACTIVE)
button.pack()


def submit():
    username = entry.get()
    print("Hello " + username)


def delete():
    entry.delete(0, END)


entry = Entry(window,
              font=("Arial", 50))
entry.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)
window.mainloop()  # place window on computer screen, listen for events