from tkinter import *

def create_window():
    #new_window= Toplevel() #Toplevel()= new window on top of other windows, linked to a bottom window
    new_window= Tk()
    # if you need to destroy the old window right after creating a new window--
    old_window.destroy() # close out of old window


old_window= Tk()
Button(old_window,text='Create new Window',command=create_window).pack()
old_window.mainloop()