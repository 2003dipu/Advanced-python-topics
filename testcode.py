from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()

    # List of common encodings to try
    encodings = ['utf-8', 'cp1252', 'latin-1', 'iso-8859-1']

    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                print(f"File opened successfully with encoding: {encoding}")
                print(file.read())
                break
        except UnicodeDecodeError:
            print(f"Failed to open file with encoding: {encoding}")

window = Tk()
button = Button(window, text='Open', command=openFile)
button.pack()
window.mainloop()
