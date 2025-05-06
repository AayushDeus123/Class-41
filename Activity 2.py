#Message Box
#Import necessary libraires
from tkinter import *
from tkinter import messagebox

#Setup Tkinter window
root = Tk()
root.title('Virus Scanner')
root.geometry('200x200')

#Function for displaying Warning Message
#This will be called once the button is clicked
#messagebox.showwarning('Window Name' , 'Text to be displayed')
def msg():
    messagebox.showwarning('Alert!' , 'Stop! Virus found')
    
#Adding Button Widget to Window
button = Button(root , text='Scan for Virus' , command=msg)
button.place(x=40 , y=80)

#Entering Mainloop event
root.mainloop()