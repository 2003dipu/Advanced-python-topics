# canvas = widget that is used to draw graphs, plots, images in a window
from tkinter import *

window= Tk()

canvas= Canvas(window,height=500,width=500)
#blueLine= canvas.create_line(0,0,500,500,fill='blue',width=5)
#redLine= canvas.create_line(0,500,500,0,fill='red',width=5)
#canvas.create_rectangle(50,50,250,250,fill='magenta')
#canvas.create_polygon(250,0,500,500,0,500,fill='pink',outline='black',width=3)
#points= [250,0,500,500,0,500]
#canvas.create_polygon(points,fill='pink',outline='black',width=3)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start= 0,extent=180,fill='green')
canvas.create_arc(0,0,400,400,fill='red',extent=180,width=5)
canvas.create_arc(0,0,400,400,fill='white',extent=180,width=5,start=180)
canvas.create_oval(160,160,240,240,fill='white',width=5)
canvas.pack()
window.mainloop()