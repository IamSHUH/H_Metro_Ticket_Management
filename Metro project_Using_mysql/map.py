from tkinter import *

#creating window
root = Tk()
root.title('H Metro Map!')

#background image
img = PhotoImage(file='images/h.png')

Label(
    root,
    image=img
).pack()

#creating a exit button
btn1 = Button(text="back",command=quit)
btn1.pack()

root.mainloop()