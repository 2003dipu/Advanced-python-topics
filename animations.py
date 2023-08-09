from tkinter import *
import time
from PIL import Image, ImageTk

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

image1 = Image.open('C:\\Users\\t\\Downloads\\earthhorizon.jpg')
image1 = image1.resize((500, 500), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(image1)
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

image2 = Image.open('C:\\Users\\t\\Downloads\\ufo.png')
photo_image = ImageTk.PhotoImage(image2)
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

try:
    while True:
        coordinates = canvas.coords(my_image)
        # print(coordinates)
        if (coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
            xVelocity= -xVelocity
        if (coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
            yVelocity= -yVelocity

        canvas.move(my_image,xVelocity,yVelocity)
        window.update()
        time.sleep(0.01)
except:
    print("The UFO image went off the edge of the window.")

window.mainloop()
