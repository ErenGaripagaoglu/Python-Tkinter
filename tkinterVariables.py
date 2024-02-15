import tkinter as tk
from tkinter import ttk

def buttonClick():
    stringVar1.set('Button clicked')

appwindow = tk.Tk()
appwindow.title('Variables')

#tkinter variable String
stringVar1 = tk.StringVar(value= 'placeholder')

label1 = ttk.Label(master= appwindow, text= 'Placeholder', textvariable= stringVar1)
label1.pack()

textbox1 = ttk.Entry(master= appwindow, textvariable= stringVar1)
textbox1.pack()

button1 = ttk.Button(master= appwindow, text= 'Click', command= buttonClick)
button1.pack()

appwindow.mainloop()