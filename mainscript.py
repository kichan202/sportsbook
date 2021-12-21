"""This is going to be the main GUI application"""
import loadodds
from tkinter import *

root = Tk()

codes = loadodds.load_code_names()


root.mainloop()