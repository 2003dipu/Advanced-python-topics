from tkinter import *
from PIL import Image, ImageTk
def submit():
    print("The temperature is "+ str(scale.get())+" degrees C")
window = Tk()

hotImage = Image.open('C:\\Users\\t\\Downloads\\hotsign.jpg')
hotImage = hotImage.resize((60, 50), Image.LANCZOS)
hotImage = ImageTk.PhotoImage(hotImage)

hotLabel = Label(image=hotImage)
hotLabel.pack()
scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL, # orientation of scale
              font=('Consolas',20),
              tickinterval=10, # adds numeric indicators for value
              #showvalue=0, # hides current value
              resolution=5,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black')
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # set current value of slider in a sophisticated way
scale.pack()

coldImage = Image.open('C:\\Users\\t\\Downloads\\icesign.jpg')
coldImage = coldImage.resize((60, 50), Image.LANCZOS)
coldImage = ImageTk.PhotoImage(coldImage)

coldLabel = Label(image=coldImage)
coldLabel.pack()
button = Button(window,text='submit',command=submit)
button.pack()
window.mainloop()
