"""from tkinter import *
from PIL import Image, ImageTk

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

window = Tk()

window.geometry("500x500")
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


image1 = Image.open('C:\\Users\\t\\Downloads\\racecar.png')
myimage = ImageTk.PhotoImage(image1)


label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()"""

# move images in a canvas
from tkinter import *

from PIL import Image, ImageTk

def move_up(event):
    canvas.move(MySobi,0,-10)
def move_down(event):
    canvas.move(MySobi,0,10)
def move_left(event):
    canvas.move(MySobi,-10,0)
def move_right(event):
    canvas.move(MySobi,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)
canvas = Canvas(window,width=500,height=500)
canvas.pack()
image1 = Image.open('C:\\Users\\t\\Downloads\\racecar.png')
myimage = ImageTk.PhotoImage(image1)
MySobi = canvas.create_image(0,0,image=myimage,anchor=NW)

window.mainloop()