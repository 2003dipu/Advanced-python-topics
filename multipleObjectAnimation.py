from tkinter import *
import time
from Ball import *



window = Tk()
WIDTH = 500
HEIGHT = 500
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,'white')
tennis_ball = Ball(canvas,0,0,50,4,3,'yellow')
foot_ball = Ball(canvas,0,0,60,5,7,'red')
strange_ball = Ball(canvas,0,0,35,2,6,'green')
black_ball = Ball(canvas,0,0,35,3,5,'black')
orange_ball = Ball(canvas,0,0,120,9,6,'orange')



try:
    while True:
        volley_ball.move()
        tennis_ball.move()
        foot_ball.move()
        strange_ball.move()
        black_ball.move()
        orange_ball.move()
       

        window.update()
        time.sleep(0.01)
except:
    print("The balls went off the edge of the window.")
window.mainloop()