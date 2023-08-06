from tkinter import *
from PIL import Image, ImageTk # disclaimer -- I have updated this library because this code editor doesn't allow
# direct access to images when i tried. 

def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved. ")
def cut():
    print("You cut some text")
def copy():
    print("You copied some text")
def paste():
    print("You pasted some text")
window= Tk()

image1 = Image.open('C:\\Users\\t\\Downloads\\file.png') # I have used some special image access path
image1 = image1.resize((40, 40), Image.LANCZOS)
openImage=ImageTk.PhotoImage(image1) # for this code editor doesn't support direct image file access
image2= Image.open('C:\\Users\\t\\Downloads\\exit.png') # or i am not aware of the right use of it
image2 = image2.resize((40, 40), Image.LANCZOS)
exitImage= ImageTk.PhotoImage(image2) # Generally from other code editors it's easy to access any image
image3= Image.open('C:\\Users\\t\\Downloads\\save.png')
image3 = image3.resize((40, 40), Image.LANCZOS) # or simply it doesn't allow me to access image easily
saveImage= ImageTk.PhotoImage(image3)

menubar= Menu(window)
window.config(menu=menubar)

fileMenu= Menu(menubar, tearoff=0,font=('MV Boli',15))

menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFile,image=openImage,compound='left')
fileMenu.add_command(label='Save',command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit,image=exitImage,compound='left')

editMenu= Menu(menubar,tearoff=0,font=('MV Boli',15))
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Cut',command=cut)
editMenu.add_command(label='Copy',command=copy)
editMenu.add_command(label='Paste',command=paste)

window.mainloop()