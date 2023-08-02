from tkinter import *
count = 0
def click():
    global count
    count+=1
    print(count)

window = Tk()

# Load the image using PhotoImage
photo = PhotoImage(file='c:/Users/t/Downloads/like button image.png')

button = Button(window,
                text='click me',
                command=click,
                font=('Comic Sans', 20),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()

window.mainloop()
