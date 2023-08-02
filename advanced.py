"""
# ***********************************
#                                Python multiprocessing
# ***********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
# ***********************************
import multiprocessing
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())

    a = Process(target = counter, args = (1,))
    b = Process(target = counter, args = (1,))
    
    a.start()
    b.start()
 

    a.join()
    b.join()
 

    print("finished in :", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()
"""


#             Python GUI WINDOW 
"""
from tkinter import *
# widgets = GUI elements : button, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets
window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Dipu Singha first GUI program")

icon = PhotoImage(file='logo.png')


window.iconphoto(True, icon)
window.mainloop() # place window on the computer screen, listen for events
"""

#             Python GUI WINDOW 

print("This is your GUI window. Your window will pop up right away.")
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("420x420")
window.title("Dipu Singha's first GUI program")

# Load the image using Pillow
image = Image.open('C:\\Users\\t\\Downloads\\aiart.jpg')

# Convert the image to a format compatible with PhotoImage
icon = ImageTk.PhotoImage(image)

# Set the window icon
window.iconphoto(True, icon)
window.config(background= "#5cfcff")

window.mainloop()
