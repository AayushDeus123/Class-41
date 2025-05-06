#Event Handle
from tkinter import *

#Create window
window = Tk()
window.title('Event Handler')
window.geometry('100x100')

#Event handler for Keypress
def handle_keypress(event):
    #Print the character associated to the key pressed
    print(event.char)
    
#Bind Keypress to the handle_keypress() function
window.bind('<Key>' , handle_keypress)

#Event handler for button click
def handle_click(event):
    print('\nThe button was clicked!')

button = Button(text = 'Click Me!')
button.pack()

#Bind click event to handle_click() function
button.bind('<Button-1>' , handle_click)
window.mainloop()