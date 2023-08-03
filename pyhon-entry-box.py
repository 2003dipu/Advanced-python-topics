from tkinter import *
# entry widget = textbox that accepts a single line of user input
def submit():
    username = entry.get()
    print("Hello " + username)
    #entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1,END)


window = Tk()

entry = Entry(window,
              font= ('Arial',50),
              fg='#00FF00',
              bg='white',
              #show='*'
                                )
#entry.insert(0, 'Write here')
entry.pack(side=LEFT)

submit_button = Button(window, text='submit button', command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='delete button', command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='Backspace button', command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()