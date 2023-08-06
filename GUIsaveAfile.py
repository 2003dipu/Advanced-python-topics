from tkinter import *
from tkinter import filedialog

def saveFile():
    file= filedialog.asksaveasfile(initialdir='G:\My Drive\Advanced Python\.txt',
                                   defaultextension='.txt',
                                   filetypes=[
                                       ('Text file','.txt'),
                                       ('HTML file','.html'),
                                       ('All files','.*')
                                   ])
    #filetext= str(text.get(1.0,END))
    filetext= input("Enter some text I guess: ")
    file.write(filetext)
    file.close()
window = Tk()
button= Button(window,text='Save',command=saveFile)
button.pack()
text= Text(window,bg='light blue',fg='black',font=('Comic Sana',23))
text.pack()
window.mainloop()