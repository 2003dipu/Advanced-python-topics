from tkinter import *
from PIL import Image, ImageTk

def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()
x = IntVar()

icon = Image.open('C:\\Users\\t\\Downloads\\python-logo.jpg')
# Resize the image to the desired dimensions (e.g., 50x50 pixels)
icon = icon.resize((50, 50), Image.LANCZOS)  # Use Image.LANCZOS for Pillow versions 8.0.0 and later
# c:\Users\t\Downloads\python-logo.jpg

python_photo = ImageTk.PhotoImage(icon)
check_button = Checkbutton(window,
                           text='I agree to something',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')
check_button.pack()
window.mainloop()
