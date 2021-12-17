#calculator app with tkinter for practice
from tkinter import *

root = Tk()
root.title('Calculator')



#define input Entry and place on the grid
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,columnspan=3,padx=10,pady=10)

#define button functions
def myClick(number):
    e.insert(0, number)    
    return

#define buttons 
button_7 = Button(root, text="7",padx=40,pady=20,command= lambda: myClick(7))
button_8 = Button(root, text="8",padx=40,pady=20,command= lambda: myClick(8))
button_9 = Button(root, text="9",padx=40,pady=20,command= lambda: myClick(9))

button_4 = Button(root, text="4",padx=40,pady=20,command= lambda: myClick(4))
button_5 = Button(root, text="5",padx=40,pady=20,command= lambda: myClick(5))
button_6 = Button(root, text="6",padx=40,pady=20,command= lambda: myClick(6))


#place buttons on the grid
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)







root.mainloop()