import tkinter as tk #import tkinter 
from tkinter import ttk

#button function
def buttonClick():
    print('Button works')

#create the app window
appwindow = tk.Tk() 
appwindow.title("Tkinter Elements")
appwindow.geometry("800x400")

#create textarea
textarea1 = tk.Text(master= appwindow)
textarea1.pack()

#create label
label1 = ttk.Label(master= appwindow, text= 'Sample label text')
label1.pack()

#create button
button1 = ttk.Button(master= appwindow, text= 'Button', command= buttonClick)
button1.pack()

#create textbox
textbox1 = ttk.Entry(master= appwindow)
textbox1.pack()

#launch the window
appwindow.mainloop() 
