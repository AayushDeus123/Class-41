from tkinter import *

def convert():
    cm = float(entry.get()) * 2.54
    result.config(text=f"{cm:.2f} cm")

root = Tk()
root.title("Length Converter App")
root.geometry('400x400')

Label(root, text="Inches:").pack()
entry = Entry(root)
entry.pack()

Button(root, text="Convert", command=convert).pack()
result = Label(root, text="")
result.pack()

root.mainloop()