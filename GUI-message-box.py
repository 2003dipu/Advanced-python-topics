from tkinter import *
from tkinter import messagebox # import messagebox library

def click():
    #messagebox.showinfo(title='This is an info message box. ',message='You are a person')
    #messagebox.showwarning(title='WARNING',message='You have a VIRUS !!!')
    #messagebox.showerror(title='ERROR',message='Something went wrong !!!')
    #if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing? '):
       # print('You did a thing !')
    #else:
        #print('You canceled a thing !')
    #if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing? '):
       # print('You retried a thing !')
    #else:
        #print('You canceled a thing !')
    #if messagebox.askyesno(title='Ask yes or no', message='Do you like cake? '):
        #print('I like cake too !')
    #else:
        #print('Why do you not like cake? ')
    #answer= messagebox.askquestion(title='ask question',message='Do you like pie? ')
    #if (answer == 'yes'):
     #   print('I like pie too')
    #else:
     #   print('Why do you not like pie? ')
    response= messagebox.askyesnocancel(title='yes no cancel',message='Do you like to code ?',icon='info')
    if (response==True):
        print('You like to code ? Good decision')
    elif(response==False):
        print('Then why are you watching a video on coding?')
    else:
        print("You have dodged the question!")

window = Tk()

button = Button(window, command = click, text='click here')
button.pack()
window.mainloop()