# listbox = a listing of selectable text items within its own container
def submit():
    food =[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered : ")

    for index in food:
        print(index)
    

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  fg='black',
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"hanu")
listbox.insert(2,"salad")
listbox.insert(3,"carrot")
listbox.insert(4,"garlic bread")
listbox.insert(5,"banana")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitButton = Button(text='submit', command=submit)
submitButton.pack()

addButton = Button(text='add', command=add)
addButton.pack()
deleteButton = Button(text='delete', command=delete)
deleteButton.pack()

window.mainloop()