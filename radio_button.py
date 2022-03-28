# radio button = similar ro checkbox, but you can only select one from a group

from tkinter import *


food = ["pizza", "hamburger", "hotdog"]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radio buttons
                              value=index,  # group radiobuttons together if they share
                              variable=x,   # assigns each radiobutton a different value
                              padx=25,      #adds padding on x-axis
                              font=("Impact", 40),
                              image=addImage[index],    # adds image to radiobutton
                              compound='left',  # adds image & text (left-side)
                              width=375)
    radiobutton.pack(anchor=W)

window.mainloop()







