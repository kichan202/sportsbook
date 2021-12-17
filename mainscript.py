"""This is going to be the main GUI application"""
import loadodds
from tkinter import *

codes = loadodds.load_code_names()

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! i Clicked a Button!")
    myLabel.pack()


#creating a label widget
#myLabel = Label(root, text="hello world!")
#shoving it onto the screen
#myLabel.pack()

#buttons
#myButton = Button(root, text="click me!", state=DISABLED)
#myButton = Button(root, text="click me!", padx=50, pady=50, fg="blue", bg="black")
myButton = Button(root, text=codes[1001], command=myClick)


myButton.pack()

root.mainloop()