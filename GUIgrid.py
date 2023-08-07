from tkinter import *
# grid= geometry manager that organizes widgets in a table like structure in a parent
window= Tk()
titleLabel= Label(window,text='Enter your info ',font=('Arial',25)).grid(row=0,column=0,columnspan=2)
def submit():
    print("Your information has been sumbitted successfully")

firstNameLabel= Label(window,text='First name : ',width=20,bg='red',fg='white').grid(row=1,column=0)
firstNameEntry= Entry(window).grid(row=1,column=1)

lastNameLabel= Label(window,text='Last name : ',bg='green',fg='white').grid(row=2,column=0)
lastNameEntry= Entry(window).grid(row=2,column=1)

emailLabel= Label(window,text='email: ',bg='blue',fg='white').grid(row=3,column=0)
emailNameEntry= Entry(window).grid(row=3,column=1)
submitButton= Button(window,text='Sumbit',command=submit).grid(row=4,column=0,columnspan=2)

window.mainloop()