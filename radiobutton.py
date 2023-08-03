# radiobutton = similar to checkbox, but you can only select one from a group
from tkinter import *
from PIL import Image, ImageTk

food = ["hanu", "thaipong", "carrot"]

def order():
    if(x.get()==0):
        print("You ordered Hanu")
    elif(x.get()==1):
        print("You ordered Thaipong")
    elif(x.get()==2):
        print("You ordered Carrot")
    else:
        print("Huh?")

window = Tk()
hanu = Image.open('C:\\Users\\t\\Downloads\\hanu.jpg')
hanuImage = ImageTk.PhotoImage(hanu)
thaipong = Image.open('C:\\Users\\t\\Downloads\\thaipong.jpg')
thaipongImage = ImageTk.PhotoImage(thaipong)
carrot = Image.open('C:\\Users\\t\\Downloads\\carrot.jpg')
carrotImage = ImageTk.PhotoImage(carrot)
foodImages = [hanuImage, thaipongImage, carrotImage]
x= IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                               text= food[index], # adds text to radiobutton
                               variable=x, # groups radiobuttons together if they share the same variable
                               value=index, # assigns each radiobutton a different value
                               padx=25, # adds padding on x-axis
                               font=('impact',30),
                               image=foodImages[index], # adds image to the radiobutton
                               compound='left',# adds image and text(left-side)
                               indicatoron=0,# eliminate circle indicators
                               width=375, # sets width of radiobutton
                                command=order ) # set command of radiobutton to function
    radiobutton.pack(anchor=W)

window.mainloop()
